import time
from playwright.sync_api import sync_playwright

FORM_URL = "https://tally.so/r/wb10YE"

# CONSTANT FILL VALUES
EMAIL = "email@gmail.com"
FIRST_NAME = "Name"
LAST_NAME = "Surname"
CITY = "NULL"
STATE = "NULL"
COUNTRY = "USA"
UNIVERSITY = "NO UNIVERSITY"
GRAD_YEAR = "2027"
LINKEDIN = "https://linkedin.com"
GITHUB = "https://github.com"
REFERRALS = "Baybol Market"
EXTRA_NOTES = "Excited to participate!"

ESSAY_1 = "I have coded in Python and JavaScript."
ESSAY_2 = "I built an AI-powered assistant."
ESSAY_3 = "I led a team project successfully."
ESSAY_4 = "I love creating useful applications."

def fill_page_1(page):
    """Page with basic info."""
    try:
        # Wait for the page to load
        page.wait_for_load_state("networkidle")
        
        # Click APPLY button
        page.click("button.sc-a7ae6819-5.ldgzwV")
        print("Clicked APPLY button")
        time.sleep(2)
        
        # Fill form fields
        page.fill("input[id='799d0e94-001a-40b6-ab14-37222a7ad29f']", FIRST_NAME)
        page.fill("input[id='cb478c5f-9f9c-4304-a77d-31287092eee5']", LAST_NAME)
        page.fill("input[id='1ac11254-a23f-4c49-91e7-f12974bb28b5']", EMAIL)
        page.fill("input[id='76c02c8f-14ec-48b4-955e-52e5cbf0af9a']", UNIVERSITY)
        page.fill("input[id='324d0da2-6711-484c-a5d0-9020f6c82d48']", CITY)
        page.fill("input[id='82d05303-68d7-4b0a-8a56-33b62cb9b240']", STATE)
        page.fill("input[id='13a4ba47-9e82-4a78-8ed5-37102ff85333']", COUNTRY)
        page.fill("input[id='ee63ca1f-bd4e-4f90-a747-3bed172078cc']", GRAD_YEAR)
        page.fill("input[id='4e9011a1-0235-428a-ac90-6fac5bc02b13']", LINKEDIN)
        page.fill("input[id='0007df8d-3dc3-46a3-9ae3-10c908abc95c']", GITHUB)

        # Click checkboxes/radios
        page.click("input[id='choice_8d197093-1465-4952-bcc9-98b2253973cd']")
        page.click("input[id='checkbox_97590e6b-d9a0-4eb8-85fa-fdcb8cc111f2']")
        page.click("input[id='checkbox_3ec4b71f-4db3-4176-bd80-648265f19c3a']")
        page.click("input[id='choice_8ef6cab0-d198-4101-aa2e-7d23b09c56b7']")
        page.click("input[id='checkbox_e7f43c2e-3575-4cb2-ad7f-5b6fc4a6495c']")

        page.fill("textarea[id='8ee6496c-34a3-4de1-88a0-4dfc248a178a']", EXTRA_NOTES)

        # Submit button
        page.click("button[type='submit']")
        print("Submitted Page 1")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error on Page 1: {e}")
        raise

def fill_page_2(page):
    """Essay questions page."""
    try:
        page.wait_for_load_state("networkidle")
        
        page.fill("textarea[id='fb347feb-65b8-42f0-8373-27ad14efac85']", ESSAY_1)
        page.fill("textarea[id='9094f951-c17d-4480-9e9d-17c6a31bc3b1']", ESSAY_2)
        page.fill("textarea[id='b0417f40-7f46-48b0-8032-6479fde06718']", ESSAY_3)

        # Click NEXT button
        page.click("button.sc-a7ae6819-5.ldgzwV")
        print("Submitted Page 2")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error on Page 2: {e}")
        raise

def fill_page_3(page):
    """Page 3 - if it exists."""
    try:
        # Wait and check if there's another page
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        print("Page 3 loaded (or skipped)")
        
    except Exception as e:
        print(f"Note on Page 3: {e}")

def fill_page_4(page):
    """Referral page."""
    try:
        page.wait_for_load_state("networkidle")
        
        page.fill("input[id='75fd9226-7f7a-45db-8155-0b7fbe638d33']", REFERRALS)
        page.fill("input[id='7c3fe31e-c2cb-42c8-ac24-0e93027699bd']", REFERRALS)
        page.fill("textarea[id='a4ea9b78-71b4-4550-9162-2930b829ce28']", EXTRA_NOTES)

        page.click("input[id='choice_ba97e9ac-e620-4ec7-9cb3-3343fdf04641']")
        
        # Final submit
        page.click("button[type='submit']")
        print("Submitted Final Page")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error on Page 4: {e}")
        raise

def run_submission(page, count):
    """Execute one complete form submission."""
    try:
        print(f"\n{'='*50}")
        print(f"   STARTING SUBMISSION #{count}")
        print(f"{'='*50}")
        
        fill_page_1(page)
        fill_page_2(page)
        fill_page_3(page)
        fill_page_4(page)

        print(f"\n{'='*50}")
        print(f"   ✓ COMPLETED SUBMISSION #{count}")
        print(f"{'='*50}\n")
        
        return True
        
    except Exception as e:
        print(f"\n✗ FAILED SUBMISSION #{count}: {e}\n")
        return False

def main():
    """Run the script 10 times with page refresh."""
    print("\n" + "="*50)
    print("  TALLY FORM AUTO-SUBMITTER")
    print("  Running 10 submissions...")
    print("="*50)
    
    with sync_playwright() as p:
        # Launch browser once
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Initial page load
            page.goto(FORM_URL)
            time.sleep(3)
            
            # Run 10 submissions
            for i in range(1, 11):
                run_submission(page, i)
                
                # Refresh page for next submission (except after the last one)
                if i < 10:
                    print(f"Refreshing page for next submission...")
                    page.reload()
                    time.sleep(3)
        
        finally:
            context.close()
            browser.close()
    
    print("\n" + "="*50)
    print("  ALL SUBMISSIONS COMPLETE!")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
