# TestProject

Запускаю только pytest AutoTests/test_CalcPage.py
pytest AutoTests/test_SearchPage.py - это заглушка

Один тест failed, так как строки различаются на один символ '1 × 2 - 3 + 1 =' == '1 * 2 - 3 + 1 ='
Другой passed

Вывод консоли:

C:\Users\lyubov\PycharmProjects\TestTask>pytest AutoTests/test_CalcPage.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\lyubov\PycharmProjects\TestTask
collected 2 items

AutoTests\test_CalcPage.py
DevTools listening on ws://127.0.0.1:51667/devtools/browser/2bef6fd7-4d86-40a9-9017-da19544bb44e
[8544:1056:0617/132553.358:ERROR:device_event_log_impl.cc(214)] [13:25:53.359] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: ╧Ёшёюхфшэхээюх ъ ёшёЄхьх єёЄЁющёЄтю эх ЁрсюЄрхЄ. (0x1F)
[8544:1056:0617/132553.441:ERROR:device_event_log_impl.cc(214)] [13:25:53.441] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: ╧Ёшёюхфшэхээюх ъ ёшёЄхьх єёЄЁющёЄтю эх ЁрсюЄрхЄ. (0x1F)
F[8544:1056:0617/132556.995:ERROR:device_event_log_impl.cc(214)] [13:25:56.998] Bluetooth: bluetooth_adapter_winrt.cc:1205 Getting Radio failed. Chrome will be unable to change the power state by itself.
[8544:1056:0617/132557.745:ERROR:device_event_log_impl.cc(214)] [13:25:57.745] Bluetooth: bluetooth_adapter_winrt.cc:1298 OnPoweredRadiosEnumerated(), Number of Powered Radios: 0
.                                                                                                                                    [100%]

============================================================================== FAILURES ===============================================================================
___________________________________________________________________ TestCalcPage.test_memory_string ___________________________________________________________________

self = <AutoTests.test_CalcPage.TestCalcPage object at 0x000001AC3F54A230>

    def test_memory_string(self):
        self.calcPage = CalcPage(self.driver)
        self.driver.find_element(By.NAME, "q").send_keys(TestData.WORD_CALC)
        self.driver.find_element(By.NAME, "btnK").click()
        self.driver.find_element(By.CLASS_NAME, "jlkklc").send_keys(TestData.CALC_EXPRESSION)
        self.driver.find_element(By.CLASS_NAME, "jlkklc").send_keys(Keys.ENTER)
        # force page up as page scrolls down for some reason
        self.driver.find_element(By.ID, "logo").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(3)
        mmr_str = self.driver.find_element(By.CLASS_NAME, "vUGUtc").text
>       assert mmr_str == TestData.CALC_EXPRESSION + " ="
E       AssertionError: assert '1 × 2 - 3 + 1 =' == '1 * 2 - 3 + 1 ='
E         - 1 * 2 - 3 + 1 =
E         ?   ^
E         + 1 × 2 - 3 + 1 =
E         ?   ^

AutoTests\test_CalcPage.py:34: AssertionError
------------------------------------------------------------------------ Captured stdout setup ------------------------------------------------------------------------

------------------------------------------------------------------------ Captured stderr setup ------------------------------------------------------------------------
[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 102.0.5005
[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome
[WDM] - Driver [C:\Users\lyubov\.wdm\drivers\chromedriver\win32\102.0.5005.61\chromedriver.exe] found in cache
------------------------------------------------------------------------- Captured log setup --------------------------------------------------------------------------
INFO     WDM:logger.py:16 ====== WebDriver manager ======
INFO     WDM:logger.py:16 Current google-chrome version is 102.0.5005
INFO     WDM:logger.py:16 Get LATEST chromedriver version for 102.0.5005 google-chrome
INFO     WDM:logger.py:16 Driver [C:\Users\lyubov\.wdm\drivers\chromedriver\win32\102.0.5005.61\chromedriver.exe] found in cache
======================================================================= short test summary info =======================================================================
FAILED AutoTests/test_CalcPage.py::TestCalcPage::test_memory_string - AssertionError: assert '1 × 2 - 3 + 1 =' == '1 * 2 - 3 + 1 ='
==================================================================== 1 failed, 1 passed in 32.82s =====================================================================

C:\Users\lyubov\PycharmProjects\TestTask>
