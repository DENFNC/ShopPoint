package schema

// Описание request при регистраций пользователя
type RegisterRequest struct {
	Username string `json:"username" validate:"required,gte=10,lte=50"`
	Email    string `json:"email" validate:"required,email"`
	Password string `json:"password" validate:"required"`
}

type LoginRequest struct {
	Email    string `json:"email" validate:"required,email"`
	Password string `json:"Password" validate:"required"`
}
