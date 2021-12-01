import os
import sys
import platform

output_html_path = os.getcwd() + "//" + "out.html"
def file_appender(input_data, output_path):
    with open(output_path, 'a') as f:
        f.writelines(input_data)

class RaportBuilder:
    def __init__(self):
        self.template = ""

    def header(self):
        header_template = "<html>"+"<head>"+"<style>"
        header_template += "body {font-size: 10pt;}\
        h2 {padding-top: 10pt;} \
        table {font-family: arial, sans-serif; border-collapse: collapse; width: 100%; table-layout: fixed ;}\
        td, th {border: 2px solid #b9b9b9; padding: 10px; text-align: center; width: 25% ;}\
        th {background-color: #d5d5d5;}\
        tr:nth-child(odd) {background-color: #eeeeee;}"
        header_template += "</style>"
        header_template += "<title>Multithreading/Multiprocessing benchmark results</title>" + "</head>" + "<body>" + "<h1>Multithreading/Multiprocessing benchmark results</h1>"
        self.template += header_template

    def enviro(self):
        enviro_template ="<h3>Execution environment</h3>"
        enviro_template += "<p>"
        enviro_template += f"Python version: {platform.python_version()}" + "<br>"
        enviro_template += f"Interpreter: {platform.python_implementation()}" + "<br>"
        enviro_template += f"Interpreter version: {sys.version}" + "<br>"
        enviro_template += f"Operating system: {platform.system()}" + "<br>"
        enviro_template += f"Operating system version: {platform.version()}" + "<br>"
        enviro_template += f"Processor: {platform.machine()}" + "<br>"
        enviro_template += f"CPUs: {os.cpu_count()}" + "<br>"
        enviro_template += "</p>"
        self.template += enviro_template


    def table_results(self, results, headers):

        table_template = "<h3>Test results</h3>"
        table_template += "<p>" + "The following table shows detailed test results:" + "</p>"
        table_template += "<table>"
        table_template += "<tr>"

        for header in headers:
            table_template += "<th>" + header + "</th>"
        table_template += "</tr>"

        if isinstance(results[0], list):
            for i in range(len(results)):
                table_template += "<tr>"
                table_template += "<td>" + f"{i+1}" + "</td>"
                for j in range(len(results[0])):
                    table_template += "<td>" + f"{results[i][j]}" + "</td>"
                table_template += "</tr>"

        if isinstance(results[0], float):
            table_template += "<tr>"
            table_template += "<td>" + "Median" + "</td>"
            for result in results:
                table_template += "<td>" + f"{result}" + "</td>"
            table_template += "</tr>"

        table_template += "</table>"
        self.template += table_template

    def footer(self):
        footer_template = "<p>" + "Autor: Marceli Toton" + "</p>"
        footer_template += "</body>" + "</html>"
        self.template += footer_template

    def get_template(self):
        return self.template


class Raport():
    def __init__(self):
        self.html_code = ""

    def add(self, part):
        self.html_code += part

#r1 = RaportHTML()
#r1.header()
#r1.enviro()
#r1.test_results()
#r1.table_results([[14.216217299999999, 13.813027], [13.455613699999997, 13.595673399999995], [13.157662500000008, 13.754953999999998]], ["Execution:", "1 thread (s)", "4 threads (s)"])
#r1.footer()
#
#file_appender(r1.get_template(), output_html_path)




