package authtoken

import (
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

type TokenManager struct {
	PrivateKey []byte
	PublicKey  []byte
}

type CustomClaims struct {
	jwt.RegisteredClaims
	SessionId string `json:"sid"`
}

func (tm *TokenManager) GenerateToken(sub string, sid string) (string, error) {
	privKey, err := jwt.ParseRSAPrivateKeyFromPEM(tm.PrivateKey)

	if err != nil {
		return "", err
	}

	claims := &CustomClaims{
		RegisteredClaims: jwt.RegisteredClaims{
			Subject:   sub,
			IssuedAt:  jwt.NewNumericDate(time.Now()),
			ExpiresAt: jwt.NewNumericDate(time.Now().Add(3600 * time.Second)),
		},
		SessionId: sid,
	}

	token := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
	tokenString, err := token.SignedString(privKey)

	if err != nil {
		return "", err
	}

	return tokenString, nil
}

func (tm *TokenManager) VerifyToken(tokenString string) (*CustomClaims, error) {
	pubKey, err := jwt.ParseRSAPublicKeyFromPEM(tm.PublicKey)

	if err != nil {
		return nil, err
	}

	parsedToken, err := jwt.ParseWithClaims(tokenString, &CustomClaims{}, func(token *jwt.Token) (interface{}, error) {
		return pubKey, nil
	})

	if err != nil {
		return nil, err
	}

	claims, ok := parsedToken.Claims.(*CustomClaims)
	if !ok {
		return nil, fmt.Errorf("invalid token claims")
	}

	return claims, nil
}
