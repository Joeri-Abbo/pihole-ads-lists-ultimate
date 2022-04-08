package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
)

func main() {
	printGopher()

	var data string

	data = getContent()

	writeContent(data)
	fmt.Println("done")
}
func writeContent(data string) {
	f, err := os.Create("ads_list.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	_, err2 := f.WriteString(data)

	if err2 != nil {
		log.Fatal(err2)
	}
}

func getContent() string {
	var data string

	scanner := bufio.NewScanner(strings.NewReader(getSources()))
	for scanner.Scan() {
		fmt.Println("fetching " + scanner.Text())

		resp, err := http.Get(scanner.Text())
		if err != nil {
			panic(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			fmt.Errorf("Status error: %v", resp.StatusCode)
		}

		content, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			fmt.Errorf("Read body: %v", err)
		}

		// read from resp.Body which is a ReadCloser
		fmt.Println("Fetched content storing in data")
		data += "\n" + string(content)

	}
	return data
}

func getSources() string {

	b, err := ioutil.ReadFile("../sources.txt")
	if err != nil {
		panic(err)
	}

	return string(b)

}

func printGopher() {

	b, err := ioutil.ReadFile("gopher.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(b))
	fmt.Println("         ")
	fmt.Println("         Gopher")
	fmt.Println("         ")
}
