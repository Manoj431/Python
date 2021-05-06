# Write a program to read text from .txt file using FileReader
# Write a program to write text to .txt file using FileWriter
import csv 

movies=[
    {"name":"MIB-1", "year":1997},
    {"name":"Transformers", "year":2007},
    {"name":"Pirates Of Carribean", "year":2003}
]

def write_file(output):
    with open("E:\Manoj\Java_io\movie.csv", "w") as film:
        writer = csv.DictWriter(film,fieldnames=["name","year"])
        writer.writeheader()
        writer.writerows(output)

def read_file():
    with open("E:\Manoj\Java_io\movie.csv","r") as page:
        read = csv.DictReader(page)

        for i in page:
            print(f"{i}")


write_file(movies)

read_file()

