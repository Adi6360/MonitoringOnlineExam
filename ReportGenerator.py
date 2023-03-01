import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def Generate_report(username,applied_penalties):

    print('****Report is ready to View!')

    pdf = canvas.Canvas('Reports/'+username+'Report.pdf', pagesize=A4)

    pdf.setFont('Helvetica',15,leading=None)
    pdf.drawCentredString(300,810,'Online Exam Proctoring System - REPORT')

    pdf.setFont('Helvetica',11,leading=None)
    pdf.drawString(190,780,'Name of Candidate: '+username)
    pdf.drawString(30,750,'Note: '+username+' has been applied with '+str(applied_penalties)+' Penalties throughout the Exam.')

    pdf.setFont('Helvetica',14,leading=None)
    pdf.drawString(30,700,'ScreenShots of False Activities by '+username+' are listed below.(If there are any)')

    # LIST over all the image in username folder and print into pdf and use the name of the file as description to the image
    
    gen_dir = 'Report Generate/'+username+'/'
    try:

        for i, img in enumerate(os.listdir(gen_dir)):

            if i%2==0 or i == 0:
                pdf.drawImage(os.path.join(gen_dir,img),60,500-i*100,width=200,height=180)
                pdf.drawString(60,500-i*100-15,img.split('.')[0])
            elif i > 1:
                pdf.drawImage(os.path.join(gen_dir,img),340,500-i*100+100,width=200,height=180)
                pdf.drawString(340,500-i*100+100-15,img.split('.')[0])
            else:
                pdf.drawImage(os.path.join(gen_dir,img),340,500,width=200,height=180)
                pdf.drawString(340,500-15,img.split('.')[0])
    except:
        print('Folder does not exists!')

    pdf.showPage()
    pdf.save()
    return True