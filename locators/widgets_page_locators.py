from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoComplitePageLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_VALUE = (
        By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTIPLE_VALUE_REMOVE = (
        By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (
        By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (
        By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (
        By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (
        By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (
        By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_SELECT_MONTH = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_SELECT_MONTH_LIST = (
        By.CSS_SELECTOR, 'div[class*="react-datepicker__month-option"]')
    DATE_AND_TIME_SELECT_YEAR = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_SELECT_YEAR_LIST = (
        By.CSS_SELECTOR, 'div[class^="react-datepicker__year-option"]')
    DATE_AND_TIME_SELECT_DAY_LIST = (
        By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    DATE_AND_TIME_SELECT_TIME_LIST = (
        By.CSS_SELECTOR, 'li[class*="react-datepicker__time-list-item "]')


class SliderPageLocators:
    SLIDER_INPUT = (
        By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_INPUT_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_VALUE = (By.CSS_SELECTOR, 'div[id="progressBar"] div')


class TabsPageLocators:
    TAB_TITLE_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TAB_TEXT_WHAT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TAB_TITLE_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TAB_TEXT_ORIGIN = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TAB_TITLE_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TAB_TEXT_USE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TAB_TITLE_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TAB_TEXT_MORE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    BUTTON_TOOL_TIPS = (
        By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    FIELD_TOOL_TIPS = (
        By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    CONTRARY_LINKS = (By.XPATH, '//*[@id="texToolTopContainer"]/a[1]')
    CONTRARY_LINKS_TOOL_TIPS = (
        By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    SECTION_LINKS = (By.XPATH, '//*[@id="texToolTopContainer"]/a[2]')
    SECTION_LINKS_TOOL_TIPS = (
        By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    # select value
    SELECT_VALUE_RESULT = (
        By.XPATH, '//*[@id="withOptGroup"]/div/div[1]/div[1]')
    SELECT_VALUE = (
        By.XPATH, '//*[@id="withOptGroup"]/div')

    SELECT_VALUE_ITEMS = (
        By.CSS_SELECTOR, 'div[class*="-option"]')

    # select one
    SELECT_ONE_RESULT = (
        By.XPATH, '//*[@id="selectOne"]/div/div[1]/div[1]')
    SELECT_ONE = (
        By.XPATH, '//*[@id="selectOne"]/div')

    SELECT_ONE_ITEMS = (
        By.CSS_SELECTOR, 'div[class*="-option"]')

    # old select
    SELECT_OLD = (
        By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    # multiselect drop down
    MULTISELECT_RESULT = (
        By.CSS_SELECTOR, 'div[class*="-multiValue"]')
    MULTISELECT = (
        By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div')

    MULTISELECT_ITEMS = (
        By.CSS_SELECTOR, 'div[class*="-option"]')

    # Standard multi select
    MULTISELECT_OLD = (
        By.CSS_SELECTOR, 'select[id="cars"]')
