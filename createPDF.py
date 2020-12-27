import os
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize

from databaseConnections import *


def createGraph(investmentDetails, profit):
    '''
    using matplotlib, it was possible to create a suitable graph to display the
    investment data by importing the data from the main program and passing
    it in via parameters
    '''
    plt.clf()
    maxMaturity = 0
    ''' the maximum maturity defines the width of the graph '''
    for row in investmentDetails:
        if row[2] > maxMaturity:
            maxMaturity = row[2]
        plt.plot([0, row[2]],[0, (row[3]-row[1])], label=row[0])
        '''
        plot each investment on the graph, using the profit over time as the
        line for which the graph is displaying
        '''
        
    profit = plt.plot([0, maxMaturity],[0, profit], label='Total Profit')
    ''' plotting the total profit, the most important label on the graph '''
    plt.legend()
    plt.ylabel('Value of Investment')
    plt.xlabel('Maturity')
    ''' labelling both of the axis '''
    plt.savefig('resources\\graph.png', bbox_inches='tight')
    '''
    saving the image file of the graph in the same location as the pdf module
    of the program so that it can be used when creating the pdf
    '''


def createPdf(path, clientDetails, investmentDetails, total, profit, remaining):
    '''
    the pdf created by the program is the final report generated about the
    client of the end user, the investment advisor
    the reportlab library allows for pdfs to be created from scratch and
    filled with the data from the main program gathered from the other
    algorithms
    this pdf will include the client's name for identification, their general
    information, their investment information, their investments and the
    graph from matplotlib visualizing the profit over time
    '''
    def bodyData(row):
        formatInvested = '£{:0,.2f}'.format(row[1])
        formatMaturity = str(row[2]) + ' Months'
        formatFinal = '£{:0,.2f}'.format(row[3])
        '''
        this involves formatting the raw data into a format that is more suitable
        for a pdf for
        '''

        column1 = Paragraph(row[0], styleBody)
        column2 = Paragraph(formatInvested, styleBody)
        column3 = Paragraph(formatMaturity, styleBody)
        column4 = Paragraph(formatFinal, styleBody)

        return [column1, column2, column3, column4]

    client = clientDetails[0] + ' ' + clientDetails[1]
    data = []
    width, height = A4

    styles = getSampleStyleSheet()
    styleBody = styles["BodyText"]
    styleBody.alignment = TA_LEFT
    styleHeader = styles["Normal"]
    styleHeader.alignment = TA_CENTER

    investmentName = Paragraph('''<b>Investment Name</b>''', styleHeader)
    amountInvested = Paragraph('''<b>Amount Invested</b>''', styleHeader)
    timeRemaining = Paragraph('''<b>Time Remaining</b>''', styleHeader)
    predictedFinal = Paragraph('''<b>Predicted Final</b>''', styleHeader)

    headers = [investmentName, amountInvested, timeRemaining, predictedFinal]

    data.append(headers)
    for row in investmentDetails:
        data.append(bodyData(row))

    table = Table(data, colWidths=[7 * cm, 3 * cm, 3 * cm, 3 * cm])
    table.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black)]))

    try:
        newpdf = canvas.Canvas(path)
        newpdf.setFont("Helvetica", 20)
        if client.endswith('s'):
            newpdf.drawCentredString(300, 775, client + '\' Investment Report')
        else:
            newpdf.drawCentredString(300, 775, client + '\'s Investment Report')
        
        newpdf.setFont("Helvetica", 10)
        newpdf.drawString(100, 720, 'First Name:')
        newpdf.drawString(100, 700, 'Last Name:')
        newpdf.drawString(100, 680, 'Phone Number:')
        newpdf.drawString(100, 660, 'Email:')
        newpdf.drawString(100, 640, 'Total To Invest:')
        newpdf.drawString(100, 620, 'Expected Profit:')
        newpdf.drawString(100, 600, 'Amount Left Uninvested:')
        
        newpdf.drawString(350, 720, clientDetails[0])
        newpdf.drawString(350, 700, clientDetails[1])
        newpdf.drawString(350, 680, clientDetails[2])
        newpdf.drawString(350, 660, clientDetails[3])
        newpdf.drawString(350, 640, '£{:0,.2f}'.format(total))
        newpdf.drawString(350, 620, '£{:0,.2f}'.format(profit))
        newpdf.drawString(350, 600, '£{:0,.2f}'.format(remaining))
        
        table.wrapOn(newpdf, width, height)
        table.drawOn(newpdf, 70, 400)
        
        newpdf.drawImage('resources\\graph.png', 90, 80, width=400, height=300)
        newpdf.save()

        return True
        
    except Exception as e:
        print(e)
        return False
