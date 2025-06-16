from playwright.sync_api import expect, sync_playwright

def yc_scraper():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False) # headless means whether the page will open on your screen, set false for debug
            context = browser.new_context()
            page = context.new_page()

            #should add regions for sections such as logging in, navigation, filtering, etc 
            
    except Exception as e: 
        print(e) # should add better except handling for timeouts(?)

def main():
    yc_scraper()

if __name__ == "__main__":
    main()