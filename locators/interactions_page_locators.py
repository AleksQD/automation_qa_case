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


class DroppablePageLocator:
    # simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    SIMPLE_DRAG = (By.CSS_SELECTOR, 'div[id="draggable"]')
    SIMPLE_DROP = (
        By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-simple"] div[id="droppable"]')

    # accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    ACCEPT_DROP = (
        By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')

    # prevent propogation
    PREVENT_TAB = (By.CSS_SELECTOR,
                   'a[id="droppableExample-tab-preventPropogation"]')
    PREVENT_DRAG = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    NOTGREEDY_OUT_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]')
    NOTGREEDY_INN_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_OUT_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]')
    GREEDY_INN_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    # revert draggable
    REVERT_TAB = (By.CSS_SELECTOR,
                  'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    REVERT_DROP = (
        By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')


class DragblePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple')
    SIMPLE_DRAGBOX = (By.CSS_SELECTOR, '#dragBox')

    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction')
    AXIS_DRAG_ONLY_X = (By.CSS_SELECTOR, '#restrictedX')
    AXIS_DRAG_ONLY_Y = (By.CSS_SELECTOR, '#restrictedY')

    CONTAINER_TAB = (
        By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction')
    CONTAINER_DRAG_IN_BOX = (
        By.CSS_SELECTOR, 'div[id="containmentWrapper"] div')
    CONTAINER_DRAG_IN_PARENT = (
        By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"] span')
