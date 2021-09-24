package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

var tpl *template.Template
var db *sql.DB

func init() {

	tpl, _ = template.ParseGlob("templates/*.gohtml")
}
func main() {

	// fmt.Println("Connecting to Database")
	var err error
	db, err = sql.Open("mysql", "root:password@tcp(localhost:3306)/test")
	if err != nil {
		panic(err.Error())
	}
	// fmt.Println("sucessfully To MySQL")
	defer db.Close()

	http.HandleFunc("/", hom)
	http.ListenAndServe("localhost:8080", nil)
}
func hom(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		tpl.ExecuteTemplate(w, "home.gohtml", nil)
		return
	}
	r.ParseForm()

	var err error
	author_id := r.FormValue("authorid")
	auther_name := r.FormValue("authername")
	first_name := r.FormValue("FirstName")
	last_name := r.FormValue("LastName")
	date_of_birth := r.FormValue("dateofbirth")
	image := r.FormValue("image")

	if author_id == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Enter Your Author ID.")
		return
	} else if auther_name == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Enter Your Author Name.")
		return
	} else if first_name == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Enter Your First Name.")
		return
	} else if last_name == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Enter Your Last Name.")
		return
	} else if date_of_birth == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Enter Your Date Of Birth.")
		return
	} else if image == "" {
		tpl.ExecuteTemplate(w, "home.gohtml", "Error to Inserting Data, Please Upload image file.")
		return
	}

	var ins *sql.Stmt
	ins, err = db.Prepare("INSERT INTO `test`.`newtable` (`AuthorID`, `AutherName`, `FirstName`, `LastName`, `DOB`, `Image`) VALUES (?, ?, ?, ?, ?, ?);")

	if err != nil {
		panic(err)
	}
	defer ins.Close()

	res, err := ins.Exec(author_id, auther_name, first_name, last_name, date_of_birth, image)
	rowsAffec, _ := res.RowsAffected()
	if err != nil || rowsAffec != 1 {
		fmt.Println("Error inserting row to database:", err)
		tpl.ExecuteTemplate(w, "home.html", "Error Inserting Your row")
		return
	}
	lastInserted, _ := res.LastInsertId()
	rowsAffected, _ := res.RowsAffected()
	fmt.Println("ID of last row inserted:", lastInserted)
	fmt.Println("number of rows affected:", rowsAffected)
	tpl.ExecuteTemplate(w, "home.gohtml", "Successfully Inserted")
}
