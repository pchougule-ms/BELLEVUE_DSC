import sys
import csv
import sys
from  msds510.Beer import Beer as br
# Added import sys and Avenger class import

# NRR comments: I didn't see that Namibia would top the list. Nice informative report.

def main():
    """interprets command line request
    Args:
        argv: an array with input and output files

    Returns:
        no return. Executed generateReport with
        collected file names.
    """
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):
    """reads an infile, sorts the content, and
       sends the sorted records and an outfile
       destination to printMarkdown to print
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the printMarkdown function with
        sorted records and an outfile to write
        the results to.
    """

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file,
                           key=lambda k: int(k['beer_servings']),
                           reverse=True)[:15]

    beer = br()
    beer.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
