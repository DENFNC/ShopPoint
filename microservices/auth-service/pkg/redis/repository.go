package redis

import (
	"context"
	"time"
)

type Repository interface {
	GetData(ctx context.Context, key string) (string, error)
	SetData(ctx context.Context, key string, val any, ttl time.Duration) error
	DelData(ctx context.Context, key string) error
}

type RedisRepository struct {
	redis RedisClient
}

func NewRedisRepository(rdb RedisClient) *RedisRepository {
	return &RedisRepository{
		redis: rdb,
	}
}

func (repo *RedisRepository) GetData(ctx context.Context, key string) (string, error) {
	result, err := repo.redis.Get(ctx, key)
	if err != nil {
		return "", err
	}

	return result, nil
}

func (repo *RedisRepository) SetData(ctx context.Context, key string, val any, ttl time.Duration) error {
	if err := repo.redis.Set(ctx, key, val, ttl); err != nil {
		return err
	}

	return nil
}

func (repo *RedisRepository) DelData(ctx context.Context, key string) error {
	if err := repo.redis.Del(ctx, key); err != nil {
		return err
	}

	return nil
}
