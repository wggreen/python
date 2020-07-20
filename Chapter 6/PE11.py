def main():
    name = input("Enter your name: ")
    blurb = input("Describe yourself: ")

    file = open("html.txt", "w")

    file.write("<html>\n")
    file.write("<head>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("  <center>\n")
    file.write("    <h1>" + name + "</h1>\n")
    file.write("  </center>\n")
    file.write("  <hr />\n")
    file.write("  " + blurb + "\n")
    file.write("  <hr />\n")
    file.write("</body>\n")
    file.write("</html>")

main()
