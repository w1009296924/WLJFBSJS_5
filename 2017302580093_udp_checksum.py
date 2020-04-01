import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import functools

class ButtonWrapper:
    def __init__(self, name, pos, color, hovercolor):
        self.widget = Button(plt.axes(pos), name, color=color, hovercolor=hovercolor)
    
    def add_callback(self, on_clicked):
        self.widget.on_clicked(on_clicked)

class InputWrapper:
    def __init__(self, name, pos, color, hovercolor, initial):
        self.widget = TextBox(plt.axes(pos), name, color=color, hovercolor=hovercolor, initial=initial)

if __name__ == '__main__':

    plt.figure(figsize=(8, 6))

    calc_checksum_btn = ButtonWrapper('Calc Checksum', [0.02, 0.02, 0.2, 0.05], 'lightgoldenrodyellow', '0.975')
    check_checksum_btn = ButtonWrapper('Check Checksum', [0.78, 0.02, 0.2, 0.05], 'lightgoldenrodyellow', '0.975')
    
    word_1 = InputWrapper('Word 1', [0.3, 0.8, 0.4, 0.08], 'lightgoldenrodyellow', '0.975', '0110011001100000')    
    word_2 = InputWrapper('Word 2', [0.3, 0.7, 0.4, 0.08], 'lightgoldenrodyellow', '0.975', '0101010101010101')
    word_3 = InputWrapper('Word 3', [0.3, 0.6, 0.4, 0.08], 'lightgoldenrodyellow', '0.975', '1000111100001100')

    checksum = InputWrapper('Checksum', [0.3, 0.45, 0.4, 0.08], 'lightgoldenrodyellow', '0.975', '')
    sum_of_words_and_checksum = InputWrapper('Sum of Words and Checksum', [0.3, 0.3, 0.4, 0.08], 'lightgoldenrodyellow', '0.975', '')

    def char_to_int(c):
        if c == '1':
            return 1
        else:
            return 0

    def add_with_wrapping(x, y):
        if len(x) < len(y):
            x, y = y, x
        diff = len(x) - len(y)
        for i in range(diff):
            y = '0' + y

        result = ''
        n = len(x)
        carry = 0
        for i in range(len(x)):
            idx = n - 1 - i
            xi = char_to_int(x[idx])
            yi = char_to_int(y[idx])
            zi = xi + yi + carry
            
            result = str(zi % 2) + result
            carry = zi // 2
        
        if carry == 1:
            return add_with_wrapping(result, '1')
        return result

    def ones_complement(x):
        result = ''
        for c in x:
            result += '1' if c == '0' else '0'
        return result

    def calc_checksum(event):
        words = [word_1.widget.text, word_2.widget.text, word_3.widget.text]
        raw_sum = functools.reduce(add_with_wrapping, words)
        checksum.widget.set_val(ones_complement(raw_sum))

    calc_checksum_btn.add_callback(calc_checksum)

    def check_checksum(event):
        words = [word_1.widget.text, word_2.widget.text, word_3.widget.text, checksum.widget.text]
        sum_of_words_and_checksum.widget.set_val(functools.reduce(add_with_wrapping, words))

    check_checksum_btn.add_callback(check_checksum)

    plt.show()