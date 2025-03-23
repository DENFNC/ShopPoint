package response

import (
	"encoding/json"
	"io"
)

func Decode[T any](payload io.ReadCloser) (T, error) {
	var decoded T

	err := json.NewDecoder(payload).Decode(&decoded)

	if err != nil {
		return decoded, err
	}

	return decoded, nil
}
