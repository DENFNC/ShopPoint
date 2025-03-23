package keys

import "os"

func LoadPrivateKey(path string) ([]byte, error) {
	privKey, err := os.ReadFile(path)

	if err != nil {
		return nil, err
	}

	return privKey, nil
}

func LoadPublicKey(path string) ([]byte, error) {
	pubKey, err := os.ReadFile(path)

	if err != nil {
		return nil, err
	}

	return pubKey, nil
}
