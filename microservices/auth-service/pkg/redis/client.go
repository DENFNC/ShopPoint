package redis

import (
	"auth/service/config"
	"context"
	"errors"
	"time"

	"github.com/redis/go-redis/v9"
)

type RedisClient interface {
	Connect(db int) error
	// Close() error
	Get(ctx context.Context, key string) (string, error)
	Set(ctx context.Context, key string, value any, ttl time.Duration) error
	Del(ctx context.Context, key string) error
}

type Client struct {
	client *redis.Client
	Config *config.Config
}

func (c *Client) Connect(db int) error {
	rdb := redis.NewClient(&redis.Options{
		Addr:     c.Config.Redis.Addr,
		Password: c.Config.Redis.Password,
		DB:       db,
	})

	if err := rdb.Ping(context.Background()).Err(); err != nil {
		return err
	}

	c.client = rdb
	return nil
}

func (c *Client) Close() error {
	if err := c.client.Close(); err != nil {
		return err
	}

	return nil
}

func (c *Client) Get(ctx context.Context, key string) (string, error) {
	val, err := c.client.Get(ctx, key).Result()
	switch {
	case err == redis.Nil:
		return "", errors.New("key does not exist")
	case err != nil:
		return "", err
	case val == "":
		return "", errors.New("value is empty")
	}

	return val, nil
}

func (c *Client) Set(ctx context.Context, key string, val any, ttl time.Duration) error {
	if err := c.client.SetEx(ctx, key, val, ttl*time.Second).Err(); err != nil {
		return err
	}

	return nil
}

func (c *Client) Del(ctx context.Context, key string) error {
	if err := c.client.Del(ctx, key).Err(); err != nil {
		return err
	}

	return nil
}
