import platform
import os
import sys

from termcolor import colored

class compilation_asset:
    def determing_x_coordinate(first_value):
        if first_value >= 1 and first_value <= 10:
            string_index = 1
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue

            else:
                return string_index
            
        elif first_value >= 11 and first_value <= 20:
            string_index = 11
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 21 and first_value <= 30:
            string_index = 21
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
        
        elif first_value >= 31 and first_value <= 40:
            string_index = 31
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
        
        elif first_value >= 41 and first_value <= 50:
            string_index = 41
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 51 and first_value <= 60:
            string_index = 51
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
        
        elif first_value >= 61 and first_value <= 70:
            string_index = 61
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 71 and first_value <= 80:
            string_index = 71
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 81 and first_value <= 90:
            string_index = 81
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
        
        elif first_value >= 91 and first_value <= 100:
            string_index = 91
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 101 and first_value <= 110:
            string_index = 101
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 111 and first_value <= 120:
            string_index = 111
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 121 and first_value <= 130:
            string_index = 121
            index_action = 0
            while string_index != first_value:
                if string_index != first_value:
                    string_index += 1
                    index_action += 1
                    continue
            else:
                return string_index
            
        elif first_value >= 131 and first_value <= 140:
            string_index = 131
            
    


    def launch_the_required_function(first_value):

        if first_value >= 11 and first_value <= 20:
            count_x = compilation_asset.one_index_column(first_value)

        elif first_value >= 21 and first_value <= 30:
            count_x = compilation_asset.two_index_column(first_value)
            
        elif first_value >= 31 and first_value <= 40:
            count_x = compilation_asset.three_index_column(first_value)
            
        elif first_value >= 41 and first_value <= 50:
            count_x =  compilation_asset.four_index_column(first_value)
            
        elif first_value >= 51 and first_value <= 60:
            count_x = compilation_asset.five_index_column(first_value)
            
        elif first_value >= 61 and first_value <= 70:
            count_x = compilation_asset.six_index_column(first_value)
            
        elif first_value >= 71 and first_value <= 80:
            count_x = compilation_asset.seven_index_column(first_value)
            
        elif first_value >= 81 and first_value <= 90:
            count_x = compilation_asset.eight_index_column(first_value)
            
        elif first_value >= 91 and first_value <= 100:
            count_x = compilation_asset.nine_index_column(first_value)

        elif first_value >= 101 and first_value <= 110:
            count_x = compilation_asset.ten_index_column(first_value)
            
        elif first_value >= 111 and first_value <= 120:
            count_x = compilation_asset.eleven_index_column(first_value)

        elif first_value >= 121 and first_value <= 130:
            count_x = compilation_asset.twelve_index_column(first_value)
            
        elif first_value >= 131 and first_value <= 140:
            count_x = compilation_asset.thirteen_index_column(first_value)

        elif first_value >= 141 and first_value <= 150:
            count_x = compilation_asset.fourteen_index_column(first_value)
            
        elif first_value >= 151 and first_value <= 160:
            count_x = compilation_asset.fifteen_index_column(first_value)
            
        elif first_value >= 161 and first_value <= 170:
            count_x = compilation_asset.sixteen_index_column(first_value)

        elif first_value >= 171 and first_value <= 180:
            count_x = compilation_asset.seventeen_index_column(first_value)
            
        elif first_value >= 181 and first_value <= 190:
            count_x = compilation_asset.eighteen_index_column(first_value)
            
        elif first_value >= 191 and first_value <= 200:
            count_x = compilation_asset.nineteen_index_column(first_value)

        elif first_value >= 201 and first_value <= 210:
            count_x = compilation_asset.twenty_index_column(first_value)

        elif first_value >= 211 and first_value <= 220:
            count_x = compilation_asset.twenty_one_index_column(first_value)
            
        elif first_value >= 221 and first_value <= 230:
            count_x = compilation_asset.twenty_two_index_column(first_value)
            
        elif first_value >= 231 and first_value <= 240:
            count_x = compilation_asset.twenty_three_index_column(first_value)
            
        elif first_value >= 241 and first_value <= 250:
            count_x = compilation_asset.twenty_four_index_column(first_value)
            
        else:
            print(colored("-----------------------------------------------------------------------------------------------\nКритическая ошибка компиляции ассета\n-----------------------------------------------------------------------------------------------"))


    def determing_y_coordinates(first_value):
        if first_value >= 1 and first_value <= 10:
            count_y = 1
            return count_y
        
        elif first_value >= 11 and first_value <= 20:
            count_y = 2
            return count_y
        
        elif first_value >= 21 and first_value <= 30:
            count_y = 3
            return count_y
        
        elif first_value >= 31 and first_value <= 40:
            count_y = 4
            return count_y
        
        elif first_value >= 41 and first_value <= 40:
            count_y = 5
            return count_y
        
        elif first_value >= 51 and first_value <= 60:
            count_y = 6
            return count_y
        
        elif first_value >= 61 and first_value <= 70:
            count_y = 7
            return count_y
        
        elif first_value >= 71 and first_value <= 80:
            count_y = 8
            return count_y
        
        elif first_value >= 81 and first_value <= 90:
            count_y = 9
            return count_y
        
        elif first_value >= 91 and first_value <= 100:
            count_y = 10
            return count_y
        
        elif first_value >= 101 and first_value <= 110:
            count_y = 11
            return count_y
        
        elif first_value >= 111 and first_value <= 120:
            count_y = 12
            return count_y
        
        elif first_value >= 121 and first_value <= 130:
            count_y = 13
            return count_y
        
        elif first_value >= 131 and first_value <= 140:
            count_y = 14
            return count_y        
        
        elif first_value >= 141 and first_value <= 150:
            count_y = 15
            return count_y
        
        elif first_value >= 151 and first_value <= 160:
            count_y = 16
            return count_y
        
        elif first_value >= 161 and first_value <= 170:
            count_y = 17
            return count_y
        
        elif first_value >= 171 and first_value <= 180:
            count_y = 18
            return count_y
        
        elif first_value >= 181 and first_value <= 190:
            count_y = 19
            return count_y
        
        elif first_value >= 191 and first_value <= 200:
            count_y = 20
            return count_y
        
        elif first_value >= 201 and first_value <= 210:
            count_y = 21
            return count_y
        
        elif first_value >= 211 and first_value <= 220:
            count_y = 22
            return count_y
        
        elif first_value >= 221 and first_value <= 230:
            count_y = 23
            return count_y
        
        elif first_value >= 231 and first_value <= 240:
            count_y = 24
            return count_y
        
        elif first_value >= 241 and first_value <= 250:
            count_y = 25
            return count_y