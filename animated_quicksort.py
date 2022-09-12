'''File: animated_quicksort.py
   Author: Mugdha Sonawane
   Description: This program illustrates the
   quicksort algorithm.
   Class: CSC 120, Spring 2020
'''

from graphics import graphics
import random
import sys

def recurse_sort(array, left, right, pivot):
    print('QS: AFTER RECURSION...')
    print('    Original data: ', str(array))
    print('    Left (sorted): ', str(left))
    print('    Right (sorted):', str(right))
    print('    Sorted data:   ', str(left + [pivot] + right))

def debug(pivot, lesser, greater, array):
    ''' This function gives the debug information.
    Arguments: pivot is the pivot value, lesser is a list
    with values lesser than the pivot, greater is a list with
    values greater than the pivot. array is the list being examined.
    Return Value: None
    '''
    print('QS: ', end='')
    print('Data in: ' + str(array))
    print('    Pivot:   ' + str(pivot))
    print('    Left:    ' + str(lesser))
    print('    Right:   ' + str(greater))

def random_generator(limit):
    '''This function generates a random number list for the algo
    to use.
    Argument: limit is the number of random values needed.
    Return Value: list with random values
    '''
    unsorted_list = []
    for i in range(limit):
        unsorted_list.append(random.randint(-50, 100))
        limit -= 1
    return unsorted_list


# quicksort algo
def quicksort(x, y, array, gui, fps):
    '''This is the quicksort algorithm.
    Arguments: x, y, gui and fps - graphics portion -
    self-explanatory. 'array' is the array that is to be sorted.
    Return Value: is a list representing the sorted array.
    '''
    if len(array) == 0:
        print('QS: The length of the input data, [], is zero or one.  Return\
        ing immediately.')
        return []
    elif len(array) == 1:
        print('QS: The length of the input data,', str(array) + ', is zero or\
        one.  Returning immediately.')
        return array
    pivot = array[0]
    lesser = [number for number in array[1:] if number <= pivot]
    greater = [number for number in array[1:] if number > pivot]
    debug(pivot, lesser, greater, array)
    if fps > 0:
        if len(lesser) > 0 or len(greater) > 0:
            anime_quicksort(x, y, pivot, array, gui, lesser, greater, fps)
    left = quicksort(x, y+70, lesser, gui, fps)  # recursion with lesser array
    right = quicksort(x+40+len(lesser)*40, y+70, greater, gui, fps)
    recurse_sort(array, left, right, pivot)
    return left + [pivot] + right

def organising_input(input_string):
    '''This function organises the data recieved from the input.
    Argument: input_string is a list of all the lines in the input.
    Return Value: is a list of unordered integers.
    '''
    # Eventhough the input is fps and everything else on the next line,
    # they aren't really taking into account the fps in your organisation
    input_string = input_string.split('\n')
    unsorted_list = []
    if 'random' in input_string[0]:
        if len(input_string[0]) == 6:
            unsorted_list = random_generator(20)
        elif input_string[0].split()[1].isdigit():
            unsorted_list = random_generator(int(input_string[0].split()[1]))
    else:
        for string in input_string:
            if string != '':
                if ' ' in string:
                    for number in string.split():
                        unsorted_list.append(int(number))
                elif ' ' not in string:
                    unsorted_list.append(int(string))
    print('INPUT DATA:', unsorted_list)
    return unsorted_list

def main():
    print("Frames per second?  (Give 0 to disable animation.)")
    fps = int(input())
    assert fps >= 0
    print("Please give the input data: ")
    input_string = input()
    unsorted_list = organising_input(input_string)
    if fps > 0:
        gui = graphics(((len(unsorted_list) * 40)+50), 800, 'quicksort')
        gui.rectangle(0, 0, ((len(unsorted_list) * 40)+50), 800)
        pivot = ''
        starting_and_ending(20, 20, unsorted_list, gui, pivot, fps)
    else:
        gui = ''
    ret_val = quicksort(20, 90, unsorted_list, gui, fps)
    if fps > 0:
        starting_and_ending(20, 740, ret_val, gui, pivot, fps)
    print('AFTER THE SORT:', str(ret_val))

''' GRAPHICS PORTION'''

def starting_and_ending(x, y, unsorted_list, gui, pivot, fps):
    '''This function is for when the unsorted and sorted lists
    need to be drawn.
    Argument: the pivot ''. only for this function. unsorted_list
    is an array. x is the abscissa. gui is a graphics object. y is
    the ordinate. fps is an integer - frames per second.
    Return Value: None
    '''
    for element in unsorted_list:
        animation_helper(pivot, element, x, y, gui, fps)
        x += 40
    # since pivot isn't present in the sorted or unsorted lists, it is ''.

def anime_quicksort(x, y, pivot, array, gui, lesser, greater, fps):
    '''This function carries out the quicksort animation.
    Argument: x is the abscissa. gui is a graphics object. y is
    the ordinate. fps is an integer - frames per second. pivot is an integer.
    lesser is a list of values less than or equal to the pivot. greater is a
    list of values larger than the pivot. array is the current list of values.
    Return Value: None
    '''
    # pivot required for making it a different colour
    if len(array) >= 1:
        for element in lesser:
            animation_helper(pivot, element, x, y, gui, fps)
            if len(lesser) == 1:
                dotted_lines(x, y, 'gold', gui)
                animation_helper(pivot, lesser[0], x, 740, gui, fps)
            x += 40
        draw_pivot(x, y, pivot, gui)
        dotted_lines(x, y, 'SeaGreen1', gui)
        draw_pivot(x, 740, pivot, gui)
        x += 40
        gui.update_frame(5)
        for element in greater:
            animation_helper(pivot, element, x, y, gui, fps)
            if len(greater) == 1:
                dotted_lines(x, y, 'gold', gui)
                animation_helper(pivot, greater[0], x, 740, gui, fps)
            x += 40

def draw_pivot(x, y, pivot, gui):
    '''This function draws the pivot in a different coloured sqaure.
    Argument: x is the abscissa. gui is a graphics object. y is
    the ordinate. pivot is an integer.
    Return Value: None
    '''
    gui.rectangle(x, y, 40, 40, 'SeaGreen1')
    gui.text(x + 12, y+15, str(pivot), 'black', 15)
    gui.line(x+40, y, x+40, y+40, 'black')

def animation_helper(pivot, element, x, y, gui, fps):
    '''This function draws a single box in the long list.
    Argument: pivot is an integer, element is the current element,
    x is the abscissa. gui is a graphics object. y is
    the ordinate. fps is an integer - frames per second.
    Return Value: None
    '''
    gui.rectangle(x, y, 40, 40, 'HotPink4')
    if element == pivot:
        gui.text(x + 12, y+15, str(element), 'SeaGreen1', 15)
    else:
        gui.text(x + 12, y+15, str(element), 'gold', 15)
    gui.line(x+40, y, x+40, y+40, 'gold')
    gui.update_frame(fps)

def dotted_lines(x, y, colour, gui):
    '''This function draws a dotted line to connect the pivot and
    the final result.
    Argument: x is the abscissa. gui is a graphics object. y is
    the ordinate. colour is a string based on the element: whether
    its a pivot or otherwise.
    Return Value:  None
    '''
    z = y+40
    while z <= 740:
        gui.line(x+20, z, x+20, z+5, colour)
        gui.update_frame(30)
        z += 20

if __name__ == '__main__':
    main()
