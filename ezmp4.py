import yt_dlp

def download_youtube_video():
    print("""                    ____            __   __________ __ __
  _________  ____  / / /____  _____/ /_ |__  /__  // // /
 / ___/ __ \/ __ \/ / __/ _ \/ ___/ __ \ /_ < /_ </ // /_
/ /__/ /_/ / /_/ / / /_/  __/ /__/ / / /__/ /__/ /__  __/
\___/\____/\____/_/\__/\___/\___/_/ /_/____/____/  /_/   
                                                         """)
    url = input("Enter the YouTube video URL: ")
    
    try:
        ydl_opts = {
            'outtmpl': '~/Downloads/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Your video was donloaded succesfully! \nIt should be found in your Downloads folder.")
        print("eztech products are all completely free. Consider supporting by checking out our other products: https://github.com/cooltech334 ")
    except Exception as e:
        print(f"An error occurred: {e}\n Check the github: https://github.com/cooltech334 for more information.")


if __name__ == "__main__":
    download_youtube_video()
