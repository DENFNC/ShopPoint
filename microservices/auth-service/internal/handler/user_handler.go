package handler

import (
	"auth/service/internal/schema"
	"auth/service/internal/service"
	"auth/service/pkg/response"
	"errors"
	"net/http"

	"github.com/jackc/pgx/v5/pgconn"
)

type AuthUserHandler struct {
	service service.UserService
}

func NewAuthUserHandler(router *http.ServeMux, service service.UserService) {
	handler := &AuthUserHandler{
		service: service,
	}

	router.HandleFunc("POST /auth/register", handler.Register())
	router.HandleFunc("POST /auth/login", handler.Login())
	// 	router.HandleFunc("/auth/logout")
	// 	router.HandleFunc("/auth/refresh")
}

func (h *AuthUserHandler) Register() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		body, err := response.HandleBody[schema.RegisterRequest](w, r)

		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		if err = h.service.CreateUser(body.Username, body.Email, body.Password); err != nil {
			var pqErr *pgconn.PgError
			if errors.As(err, &pqErr) && pqErr.Code == "23505" {
				http.Error(w, "User with this username already exists", http.StatusConflict)
				return
			}
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
	}
}

func (h *AuthUserHandler) Login() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		body, err := response.HandleBody[schema.LoginRequest](w, r)

		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		result, err := h.service.GetUser(body.Email, body.Password)

		if err != nil {
			http.Error(w, "Incorrect user or password", http.StatusNotFound)
			return
		}

		response.Json(w, result, http.StatusOK)
	}
}
