# ATM Controller

## Cloning
To clone the project, run the following in terminal:
```bash
git clone https://github.com/nadernamini/ATM.git
```
 
## Build
The project is written in Python3 and does not require any build.

## Testing
To test the `ATM` class in `atm_module.py`, use the `ATMModuleTests` class in `atm_tests.py`.
To add a unit test, simply add a method to the `ATMModuleTests` class by using the `def [function_name](self):` signature.
A sample test is available in `atm_tests.py` and shown below:
```python
def test_basic(self):
        atm = atm_module.ATM()
        atm.reset_session()
        self.assertTrue(atm.insert_card("1234567890123456"))
        self.assertFalse(atm.enter_pin("0042"))
        self.assertTrue(atm.enter_pin("0000"))
        self.assertListEqual(atm.list_accounts(), ['Checkings 1', ' Checkings 2', 'Savings 1'])
        self.assertTrue(atm.select_account(0))
        self.assertEqual(atm.view_balance(), 10000)
        self.assertTrue(atm.deposit_money(1000), 10000)
        self.assertTrue(atm.withdraw_money(3402), 10000)
```
