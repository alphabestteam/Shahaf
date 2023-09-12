import requests, time, threading

def download_url(url: str) -> None:
    image = requests.get(url)

    with open('image.jpg', 'wb') as file:
        file.write(image.content)

def timer(func, *args):
    before = time.time()

    func(*args)

    after = time.time()

    print(f'It took the program {after - before} seconds')

def main():
    thread_one = threading.Thread(timer(download_url, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png'))
    thread_two = threading.Thread(timer(download_url, 'https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png'))
    thread_three = threading.Thread(timer(download_url, 'https://github.githubassets.com/images/modules/open_graph/github-mark.png'))
    thread_four = threading.Thread(timer(download_url, 'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png'))

    thread_one.start()
    thread_two.start()
    thread_three.start()
    thread_four.start()


if __name__ == '__main__':
    main()