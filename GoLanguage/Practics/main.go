package main

import (
	// "go/printer"
	"fmt"
	"os"
)
var path = "app.txt"
func isError(err error) bool {
    if err != nil {
        fmt.Println(err.Error())
    }
    return (err != nil)
}

func main(){
	// fmt.Println("Create DB file")
	var file, err = os.OpenFile(path, os.O_RDWR, 0644)
	if isError(err){
		return
	}
	defer file.Close()
}
