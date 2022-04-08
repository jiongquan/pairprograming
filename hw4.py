import random
import time
import matplotlib.pyplot as plt
import searching
import sorting
import misc

# [You must install a package called matplotlib](
# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#interpreter-settings) To
# install matplotlib package goto menue file->settings->project->project interpreter -> + sign on the right -> search
# matplotlib and install

## The following code is to test all the above functions and plot the results.
# You can comment the following section to test your implementations one by one.
## However, once you are done implementing each of the functions, you should test
# the whole script using the following code.
## Although you dont have to edit the following code much,
# its a good idea to take a good look and make sense out of it.

if __name__ == "__main__":
    # In this function, we will compute the time taken by each of the functions that we have implemented
    ################################# Experimental setup #################################
    time_dictionary = {}
    max_values = 1000000
    # max_iteration = 1000
    max_iteration = 100
    # iteration_per_input_set = 100
    iteration_per_input_set = 10
    random.seed(123)  # If you comment this line, you will get different list every
    # list_lengths = list(range(1000, 1000000, 10000))
    list_lengths = list(range(10, 1001, 100))
    # defining a list of function
    search_function_list = [searching.linear_search_iterative, searching.linear_search_recursive,
                            searching.binary_search_iterative, searching.binary_search_recursive]
    sort_function_list = [sorting.bubble_sort, sorting.insertion_sort, sorting.counting_sort, sorting.merge_sort]
    misc_function_list = [misc.is_sorted]

    for length in list_lengths:  # testing for the different length of list
        input_list = [int(random.random() * max_values) for i in range(length)]
        # Generating a list of given length with random numbers
        # For testing the correctness of the sorting algorithms, we need to have the sorted list
        sys_sorted_list = sorted(input_list)  # Returns a sorted list without modifying the actual list
        for function in sort_function_list:  # test each function
            time_estimate = 0
            for exp in range(iteration_per_input_set):
                start = time.time()  # noting the start time for selection_sort
                sorted_list = function(input_list)
                elapsed_time_lc = (time.time() - start)  # computing the elapsed time in selection_sorting
                time_estimate = time_estimate + elapsed_time_lc
            # averaging the time over multiple runs for the same input
            est_elapsed_time = time_estimate / iteration_per_input_set

            if sorted_list == sys_sorted_list:  # Checking is selection_sort is working properly
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [est_elapsed_time]  # noting time if the sorting algo
                    # is working properly
                else:
                    time_dictionary[function.__name__].append(est_elapsed_time)  # noting time if the sorting algo
                    # is working properly
            else:  # Adding failed instead of noting time
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [-1]
                else:
                    time_dictionary[function.__name__].append(-1)

        # Let's test for the is_sorted() function
        for function in misc_function_list:  # test each function
            time_estimate = 0
            for exp in range(iteration_per_input_set):
                start = time.time()
                is_sorted_result1 = function(input_list)
                is_sorted_result2 = function(sys_sorted_list)
                elapsed_time_lc = (time.time() - start)
                time_estimate = time_estimate + elapsed_time_lc
            # averaging the time over multiple runs for the same input
            est_elapsed_time = time_estimate / iteration_per_input_set
            # How to find if the input_list was actually sorted or not
            the_input_list_sorted = input_list == sorted(input_list)

            if not is_sorted_result1 and is_sorted_result2 and the_input_list_sorted:
                # assuming that the random list won't be sorted, which may not be accurate
                # can you think of a better and more accurate way to do it? look above and see how did I compute
                # the_input_list_sorted and what does it mean!
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [est_elapsed_time]  # noting time if is_sorted
                    # is working properly
                else:
                    time_dictionary[function.__name__].append(est_elapsed_time)  # noting time if is_sorted
                    # is working properly
            else:  # Adding failed instead of noting time
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [-1]
                else:
                    time_dictionary[function.__name__].append(-1)

        # What about the correctness of the searching algorithms, how to test them
        # We will generate a list of keys to be searched. Some of them will exist in the input_list and some of them
        # won't. then search them in the input list, save the results in a list of True and False.
        from random import shuffle  # this shuffles the input list, helps generate the existing systems

        existing_key_list = input_list[:]  # copying the input list
        shuffle(existing_key_list)
        random_list = [int(random.random() * max_values // 2) for i in range(length)]
        not_existing_key_list = [item for item in random_list if item not in input_list]
        search_keys = existing_key_list + not_existing_key_list
        correct_search_results = []
        for key in search_keys:
            if key in input_list:
                correct_search_results.append(True)
            else:
                correct_search_results.append(False)

        for function in search_function_list:  # test each function
            time_estimate = 0
            search_results = []
            for key in search_keys:
                for exp in range(iteration_per_input_set):  # each search will occur certain number of times.
                    start = time.time()
                    found = function(input_list, key)
                    elapsed_time_lc = (time.time() - start)  # computing the elapsed time in searching
                    search_results.append(found)
                    time_estimate = time_estimate + elapsed_time_lc
            est_elapsed_time = time_estimate / iteration_per_input_set

            if search_results == correct_search_results:  # Checking if the search function is working properly
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [est_elapsed_time]
                    # noting time if the search function is working properly
                else:
                    time_dictionary[function.__name__].append(est_elapsed_time)
                    # if the search function is working properly
            else:  # Adding failed instead of noting time
                if function.__name__ not in time_dictionary:
                    time_dictionary[function.__name__] = [-1]
                else:
                    time_dictionary[function.__name__].append(-1)

if __name__ == "__main__":
    # printing the analysis dictionary
    # If everything worked fine, you won't see a -1 keyword anywhere in the output
    misc.print_dictionary(time_dictionary)
    # plotting the time taken by each algorithm
    # Initially almost everything would be -1
    # In the end, there will be 5 different lines on the plot
    # Sometimes the plot lines may not be visible because they may be on top of each other
    for key in time_dictionary:
        plt.plot(time_dictionary[key], '-o')

    plt.title('Empirical Analysis of Computational Complexities')
    plt.legend(list(time_dictionary.keys()))
    plt.ylabel('Computation time')
    plt.xlabel('Number of elements')
    plt.xticks(range(len(list_lengths)), list_lengths)
    plt.show()