import asyncio
from pydoll.browser import Chrome
from pydoll.browser.options import ChromiumOptions

async def main():
    options = ChromiumOptions()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument('--disable-blink-features=AutomationControlled')

    async with Chrome(options=options) as browser:
        tab = await browser.start()
        await tab.go_to('https://www.reddit.com/r/dankmemes/best/')
        await tab.go_to('https://www.reddit.com/r/dankmemes/best/')




        title_element = await tab.query("//a//faceplate-screen-reader-content")
        print(await title_element.text)




        image_element = await tab.find(class_name="post-background-image-filter")
        image = image_element.get_attribute("src")        
        print(image)


        upvote_number = await tab.query("//span//faceplate-number[@number]",find_all=True,timeout=5)
        print(upvote_number)





        # upvote_container = await tab.query('data-post-click-location="vote"')
        # print(await upvote_container.inner_html)

        # descendants = await upvote_container.get_children_elements(max_depth=2)


        await tab.execute_script("window.scrollBy(0, 1000)")
        await asyncio.sleep(1000000)



        browser.close()


if __name__ == "__main__":
    asyncio.run(main())

