from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEMS = (By.CSS_SELECTOR,
                  'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEMS = (By.CSS_SELECTOR,
                  'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEMS = (By.CSS_SELECTOR,
                  'ul[id="verticalListContainer"] li')
    LIST_ITEMS_ACTIVE = (By.CSS_SELECTOR,
                         'ul[id="verticalListContainer"] li[class*="active"]')

    GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEMS = (By.CSS_SELECTOR,
                  'div[id="gridContainer"] li')
    GRID_ITEMS_ACTIVE = (By.CSS_SELECTOR,
                         'div[id="gridContainer"] li[class*="active"]')


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
