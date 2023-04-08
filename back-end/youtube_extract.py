from pytube import YouTube,Channel
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import google.auth
from googleapiclient.discovery import build
import scrapetube
from datetime import date,datetime
import pdfkit

youtube = build('youtube', 'v3',developerKey='your_youtube_data_api_key')

def generate_pdf():
    pdfkit.from_file('./Program outputs/final_pdf.html', './Program outputs/output.pdf', options={
        'page-size': 'A4',
        'orientation':'Landscape',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0.5in',
        'margin-left': '0in',
        'no-stop-slow-scripts': True,
        'header-right': '[page]',
        'footer-right': 'Page [page]'
    })


def txttohtml():
    with open("./Program outputs/final_pdf.txt") as f:
        with open("./Program outputs/final_pdf.html", "w") as f1:
            for line in f:
                f1.write(line)

def myimg():
    data = pd.read_csv('./Program outputs/data.csv')
    data = data.sort_values(by=['Total Views'], ascending=False)
    top10 = data.head(10)
    plt.figure(figsize=(8,5))
    plt.bar(top10['Id'], top10['Total Views'])
    plt.title('Top 10 Videos by Views')
    plt.xlabel('Id')
    plt.ylabel('Total Views')
    plt.xticks(rotation=90)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    html = f'<div><img src="data:image/png;base64,{image_base64}"></div>'
    with open('./Program outputs/top10.html', 'w') as file:
        file.write(html)

    
def channel_info(yt,mail):
    ch_request = youtube.channels().list(part='statistics',id=yt.channel_id)
    ch_request1 = youtube.channels().list(part='snippet',id=yt.channel_id)
    ch_request2 = youtube.channels().list(part='topicDetails',id=yt.channel_id)
    
    ch_response = ch_request.execute()
    ch_response1 = ch_request1.execute()
    ch_response2 = ch_request2.execute()
    
    topic = ch_response2['items'][0]['topicDetails']['topicCategories']
    
    sub = ch_response['items'][0]['statistics']['subscriberCount']
    vid = ch_response['items'][0]['statistics']['videoCount']
    views = ch_response['items'][0]['statistics']['viewCount']
    name = ch_response1['items'][0]['snippet']['title']
    description = ch_response1['items'][0]['snippet']['description']
    publish = ch_response1['items'][0]['snippet']['publishedAt']
    try:
        country = ch_response1['items'][0]['snippet']['country']
    except:
        country="Not Provided"
    videos = scrapetube.get_channel(yt.channel_id)
    cnt=0
    
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open("pdf_template1.html") as f:
        with open("./Program outputs/final_pdf.txt", "w") as f1:
            for line in f:
                if "mydate" in line:
                    f1.write(line.replace("mydate", str(today)))
                elif "mytime" in line:
                    f1.write(line.replace("mytime", str(current_time)))
                elif "useremail" in line:
                    f1.write(line.replace("useremail", str(mail)))
                elif "mysub" in line:
                    f1.write(line.replace("mysub", str(sub)))
                elif "vidcnt" in line:
                    f1.write(line.replace("vidcnt", str(vid)))
                elif "viewcnt" in line:
                    f1.write(line.replace("viewcnt", str(views)))
                elif "pdate" in line:
                    f1.write(line.replace("pdate", str(publish)))
                elif "cname" in line:
                    f1.write(line.replace("cname", str(name)))
                elif "mycountry" in line:
                    f1.write(line.replace("mycountry", str(country)))
                elif "ccateg" in line:
                    temp=""
                    for i in topic:
                        i=i.replace("https://en.wikipedia.org/wiki/","")
                        temp+=str(i)+","
                    f1.write(line.replace("ccateg", str(temp)))
                else:
                    f1.write(line)
    
    file1 = open("./Program outputs/data.csv", "w")
    file1.write("Id,Total Views\n")
    file1.close()
    
    tot_amt=0
    tot_views=0
    for title in videos:
        cnt+=1
        print(cnt)
        vidlink=("https://www.youtube.com/watch?v="+str(title['videoId']))
        yt1 = YouTube(vidlink)
        tot_amt,tot_views=video_info(yt1,cnt,vidlink,tot_amt,tot_views)
    myimg()
    with open('./Program outputs/top10.html', 'r') as source_file:
        content = source_file.read()
    file2=open("./Program outputs/final_pdf.txt","a")
    file2.write('<tr><td><h5 class="text-success"><strong>Grand Total</strong></h5></td><td>&nbsp;</td><td><h5 class="text-success"><strong>'+str(format(tot_views,',d'))+'</strong></h5></td><td>&nbsp;</td><td>&nbsp;</td><td><h5 class="text-success"><strong>$'+str(round(tot_amt,2))+'</strong></h5></td></tr>')
    file2.write('</tbody></table></div></div></div></div><center><div style="margin-right:auto;margin-left:auto;margin-bottom:30px;">'+str(content)+'</div></center><div class="invoice-footer">Contact me at<a href="https://www.github.com/Rharikrishna02" class="btn"><i class="fa-brands fa-github"></i> GitHub</a><a href="mailto:rharikrishna02@gmail.com" class="btn"><i class="fa-solid fa-envelope"></i> GMail</a><a href="https://www.linkedin.com/in/harikrishna-r-1a034a221/" class="btn"><i class="fa-brands fa-linkedin-in"></i> LinkedIn</a></div></div></div></div></div></div></div></body></html>')
    file2.close()
    txttohtml()
    generate_pdf()

def video_info(yt,cnt,vidlink,tot_amt,tot_views):
    file1 = open("./Program outputs/data.csv", "a")
    file2=open("./Program outputs/final_pdf.txt","a")
    
    try:
        amount=round((yt.views)*0.018,2)
        tot_amt+=amount
        tot_views+=yt.views
        file1.write(str(yt.video_id)+","+str(yt.views)+"\n")
        file1.close()
        pubdate=str(yt.publish_date)
        file2.write('<tr><td><p>'+str(yt.title)+'</p><a href="'+str(vidlink)+'"><p class="m-0 text-muted">'+str(vidlink)+'</p></td><td>'+str(format(yt.length,',d'))+'</td><td>'+str(format(yt.views,',d'))+'</td><td><a href="'+str(yt.thumbnail_url)+'">Thumbnail</a></td><td>'+str(pubdate.replace(" 00:00:00",""))+'</td><td>$'+str(amount)+'</td></tr>')
        file2.close()
        print('Done')
    except:
        print('Error')
    return tot_amt,tot_views
    
    
def uinput(link,mail):
    yt = YouTube(link)
    channel_info(yt,mail)
