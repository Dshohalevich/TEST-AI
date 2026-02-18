package main

import (
	"embed"
	"fmt"
	"log"
	"net/http"
	"os/exec"
	"runtime"
	"time"
)

//go:embed web/index.html
var webFS embed.FS

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		content, err := webFS.ReadFile("web/index.html")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "text/html; charset=utf-8")
		_, _ = w.Write(content)
	})

	listenAddr := "0.0.0.0:8080"
	openURL := "http://127.0.0.1:8080"

	go func() {
		time.Sleep(600 * time.Millisecond)
		openBrowser(openURL)
	}()

	fmt.Println("iOS-style engineering calculator is running:", openURL)
	fmt.Println("If the browser didn't open, paste this into browser:", openURL)
	fmt.Println("Press Ctrl+C to stop.")
	log.Fatal(http.ListenAndServe(listenAddr, mux))
}

func openBrowser(url string) {
	if runtime.GOOS == "windows" {
		_ = exec.Command("rundll32", "url.dll,FileProtocolHandler", url).Start()
		return
	}
	_ = exec.Command("xdg-open", url).Start()
}
