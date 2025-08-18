from termcolor import colored

class obtaining_the_necessary_information:
    class definition_what_line_breaks:
        def space(count_x):
            if count_x == 0:
                count_space = ""
                return count_space
            elif count_x == 1:
                count_space = " "
                return count_space
            elif count_x == 2:
                count_space = "  "
                return count_space
            elif count_x == 3:
                count_space = "   "
                return count_space
            elif count_x == 4:
                count_space = "    "
                return count_space
            elif count_x == 5:
                count_space = "     "
                return count_space
            elif count_x == 6:
                count_space = "      "
                return count_space
            elif count_x == 7:
                count_space = "       "
                return count_space
            elif count_space == 8:
                count_space = "        "
                return count_space
            elif count_space == 9:
                count_space = "         "
                return count_space
        
        def down(count_y):
            if count_y == 0:
                count_down = ""
                return count_down            
            elif count_y == 1:
                count_down = "\n"
                return count_down
            elif count_y == 2:
                count_down = "\n\n"
                return count_down
            elif count_y == 3:
                count_down = "\n\n\n"
                return count_down
            elif count_y == 4:
                count_down = "\n\n\n\n"
                return count_down
            elif count_y == 5:
                count_down = "\n\n\n\n\n"
                return count_down
            elif count_y == 6:
                count_down = "\n\n\n\n\n\n"
                return count_down
            elif count_y == 7:
                count_down = "\n\n\n\n\n\n\n"
                return count_down
            elif count_y == 8:
                count_down = "\n\n\n\n\n\n\n\n"
                return count_down
            elif count_y == 9:
                count_down = "\n\n\n\n\n\n\n\n\n"
                return count_down
            

    def options(first_value):
        if first_value >= 1 and first_value <= 10:
            count_x = obtaining_the_necessary_information.one(first_value)
            return count_x
        elif first_value >= 11 and first_value <= 20:
            count_x = obtaining_the_necessary_information.two(first_value)
            return count_x
        elif first_value >= 21 and first_value <= 30:
            count_x = obtaining_the_necessary_information.three(first_value)
            return count_x
        elif first_value >= 31 and first_value <= 40:
            count_x = obtaining_the_necessary_information.four(first_value)
            return count_x
        elif first_value >= 41 and first_value <= 50:
            count_x = obtaining_the_necessary_information.five(first_value)
            return count_x
        elif first_value >= 51 and first_value <= 60:
            count_x = obtaining_the_necessary_information.six(first_value)
            return count_x
        elif first_value >= 61 and first_value <= 70:
            count_x = obtaining_the_necessary_information.seven(first_value)
            return count_x
        elif first_value >= 71 and first_value <= 80:
            count_x = obtaining_the_necessary_information.eight(first_value)
            return count_x
        elif first_value >= 81 and first_value <= 90:
            count_x = obtaining_the_necessary_information.nine(first_value)
            return count_x
        elif first_value >= 91 and first_value <= 100:
            count_x = obtaining_the_necessary_information.ten(first_value)
            return count_x
        elif first_value >= 101 and first_value <= 110:
            count_x = obtaining_the_necessary_information.eleven(first_value)
            return count_x
        elif first_value >= 111 and first_value <= 120:
            count_x = obtaining_the_necessary_information.twelve(first_value)
            return count_x
        elif first_value >= 121 and first_value <= 130:
            count_x = obtaining_the_necessary_information.thirteen(first_value)
            return count_x
        elif first_value >= 131 and first_value <= 140:
            count_x = obtaining_the_necessary_information.fourteen(first_value)
            return count_x
        elif first_value >= 141 and first_value <= 150:
            count_x = obtaining_the_necessary_information.fifteen(first_value)
            return count_x
        elif first_value >= 151 and first_value <= 160:
            count_x = obtaining_the_necessary_information.sixteen(first_value)
            return count_x
        elif first_value >= 161 and first_value <= 170:
            count_x = obtaining_the_necessary_information.seventeen(first_value)
            return count_x
        elif first_value >= 171 and first_value <= 180:
            count_x = obtaining_the_necessary_information.eighteen(first_value)
            return count_x
        elif first_value >= 181 and first_value <= 190:
            count_x = obtaining_the_necessary_information.nineteen(first_value)
            return count_x
        elif first_value >= 191 and first_value <= 200:
            count_x = obtaining_the_necessary_information.twenty(first_value)
            return count_x
        elif first_value >= 201 and first_value <= 210:
            count_x = obtaining_the_necessary_information.twenty_one(first_value)
            return count_x
        elif first_value >= 211 and first_value <= 220:
            count_x = obtaining_the_necessary_information.twenty_two(first_value)
            return count_x
        elif first_value >= 221 and first_value <= 230:
            count_x = obtaining_the_necessary_information.twenty_three(first_value)
            return count_x
        elif first_value >= 231 and first_value <= 240:
            count_x = obtaining_the_necessary_information.twenty_four(first_value)
            return count_x
        elif first_value >= 241 and first_value <= 250:
            count_x = obtaining_the_necessary_information.twenty_five(first_value)
            return count_x
        
        else:
            print(colored("-----------------------------------------------------------------------------------------------\nКритическая ошибка компиляции ассета\n-----------------------------------------------------------------------------------------------" , "red"))

    def one(first_value):
        if first_value == 1:
            return 0
        elif first_value == 2:
            return 1
        elif first_value == 3:
            return 2
        elif first_value == 4:
            return 3
        elif first_value == 5:
            return 4
        elif first_value == 6:
            return 5
        elif first_value == 7:
            return 6
        elif first_value == 8:
            return 7
        elif first_value == 9:
            return 8
        elif first_value == 10:
            return 9
        
        else:
            return "Error"
    
    def two(first_value):
        if first_value == 11:
            return 0
        elif first_value == 12:
            return 1
        elif first_value == 13:
            return 2
        elif first_value == 14:
            return 3
        elif first_value == 15:
            return 4
        elif first_value == 16:
            return 5
        elif first_value == 17:
            return 6
        elif first_value == 18:
            return 7
        elif first_value == 19:
            return 8
        elif first_value == 20:
            return 9

        else:
            return "Error"
    
    def three(first_value):
        if first_value == 21:
            return 0
        elif first_value == 22:
            return 1
        elif first_value == 23:
            return 2
        elif first_value == 24:
            return 3
        elif first_value == 25:
            return 4
        elif first_value == 26:
            return 5
        elif first_value == 27:
            return 6
        elif first_value == 28:
            return 7
        elif first_value == 29:
            return 8
        elif first_value == 30:
            return 9
        
        else:
            return "Error"

    def four(first_value):
        if first_value == 31:
            return 0
        elif first_value == 32:
            return 1
        elif first_value == 33:
            return 2
        elif first_value == 34:
            return 3
        elif first_value == 35:
            return 4
        elif first_value == 36:
            return 5
        elif first_value == 37:
            return 6
        elif first_value == 38:
            return 7
        elif first_value == 39:
            return 8
        elif first_value == 40:
            return 9
        
    def five(first_value):
        if first_value == 41:
            return 0
        elif first_value == 42:
            return 1
        elif first_value == 43:
            return 2
        elif first_value == 44:
            return 3
        elif first_value == 45:
            return 4
        elif first_value == 46:
            return 5
        elif first_value == 47:
            return 6
        elif first_value == 48:
            return 7
        elif first_value == 49:
            return 8
        elif first_value == 50:
            return 9
    
    def six(first_value):
        if first_value == 51:
            return 0
        elif first_value == 52:
            return 1
        elif first_value == 53:
            return 2
        elif first_value == 54:
            return 3
        elif first_value == 55:
            return 4
        elif first_value == 56:
            return 5
        elif first_value == 57:
            return 6
        elif first_value == 58:
            return 7
        elif first_value == 59:
            return 8
        elif first_value == 60:
            return 9
    
    def seven(first_value):
        if first_value == 61:
            return 0
        elif first_value == 62:
            return 1
        elif first_value == 63:
            return 2
        elif first_value == 64:
            return 3
        elif first_value == 65:
            return 4
        elif first_value == 66:
            return 5
        elif first_value == 67:
            return 6
        elif first_value == 68:
            return 7
        elif first_value == 69:
            return 8
        elif first_value == 70:
            return 9
    
    def eight(first_value):
        if first_value == 71:
            return 0
        elif first_value == 72:
            return 1
        elif first_value == 73:
            return 2
        elif first_value == 74:
            return 3
        elif first_value == 75:
            return 4
        elif first_value == 76:
            return 5
        elif first_value == 77:
            return 6
        elif first_value == 78:
            return 7
        elif first_value == 79:
            return 8
        elif first_value == 80:
            return 9
    
    def nine(first_value):
        if first_value == 81:
            return 0
        elif first_value == 82:
            return 1
        elif first_value == 83:
            return 2
        elif first_value == 84:
            return 3
        elif first_value == 85:
            return 4
        elif first_value == 86:
            return 5
        elif first_value == 87:
            return 6
        elif first_value == 88:
            return 7
        elif first_value == 89:
            return 8
        elif first_value == 90:
            return 9
        
    def ten(first_value):
        if first_value == 91:
            return 0
        elif first_value == 92:
            return 1
        elif first_value == 93:
            return 2
        elif first_value == 94:
            return 3
        elif first_value == 95:
            return 4
        elif first_value == 96:
            return 5
        elif first_value == 97:
            return 6
        elif first_value == 98:
            return 7
        elif first_value == 99:
            return 8
        elif first_value == 100:
            return 9
    
    def eleven(first_value):
        if first_value == 101:
            return 0
        elif first_value == 102:
            return 1
        elif first_value == 103:
            return 2
        elif first_value == 104:
            return 3
        elif first_value == 105:
            return 4
        elif first_value == 106:
            return 5
        elif first_value == 107:
            return 6
        elif first_value == 108:
            return 7
        elif first_value == 109:
            return 8
        elif first_value == 110:
            return 9
    
    def twelve(first_value):
        if first_value == 111:
            return 0
        elif first_value == 112:
            return 1
        elif first_value == 113:
            return 2
        elif first_value == 114:
            return 3
        elif first_value == 115:
            return 4
        elif first_value == 116:
            return 5
        elif first_value == 117:
            return 6
        elif first_value == 118:
            return 7
        elif first_value == 119:
            return 8
        elif first_value == 120:
            return 9
    
    def thirteen(first_value):
        if first_value == 121:
            return 0
        elif first_value == 122:
            return 1
        elif first_value == 123:
            return 2
        elif first_value == 124:
            return 3
        elif first_value == 125:
            return 4
        elif first_value == 126:
            return 5
        elif first_value == 127:
            return 6
        elif first_value == 128:
            return 7
        elif first_value == 129:
            return 8
        elif first_value == 130:
            return 9
    
    def fourteen(first_value):
        if first_value == 131:
            return 0
        elif first_value == 132:
            return 1
        elif first_value == 133:
            return 2
        elif first_value == 134:
            return 3
        elif first_value == 135:
            return 4
        elif first_value == 136:
            return 5
        elif first_value == 137:
            return 6
        elif first_value == 138:
            return 7
        elif first_value == 139:
            return 8
        elif first_value == 140:
            return 9
        
    def fifteen(first_value):
        if first_value == 141:
            return 0
        elif first_value == 142:
            return 1
        elif first_value == 143:
            return 2
        elif first_value == 144:
            return 3
        elif first_value == 145:
            return 4
        elif first_value == 146:
            return 5
        elif first_value == 147:
            return 6
        elif first_value == 148:
            return 7
        elif first_value == 149:
            return 8
        elif first_value == 150:
            return 9

    def sixteen(first_value):
        if first_value == 151:
            return 0
        elif first_value == 152:
            return 1
        elif first_value == 153:
            return 2
        elif first_value == 154:
            return 3
        elif first_value == 155:
            return 4
        elif first_value == 156:
            return 5
        elif first_value == 157:
            return 6
        elif first_value == 158:
            return 7
        elif first_value == 159:
            return 8
        elif first_value == 160:
            return 9
    
    def seventeen(first_value):
        if first_value == 161:
            return 0
        elif first_value == 162:
            return 1
        elif first_value == 163:
            return 2
        elif first_value == 164:
            return 3
        elif first_value == 165:
            return 4
        elif first_value == 166:
            return 5
        elif first_value == 167:
            return 6
        elif first_value == 168:
            return 7
        elif first_value == 169:
            return 8
        elif first_value == 170:
            return 9
    
    def eighteen(first_value):
        if first_value == 171:
            return 0
        elif first_value == 172:
            return 1
        elif first_value == 173:
            return 2
        elif first_value == 174:
            return 3
        elif first_value == 175:
            return 4
        elif first_value == 176:
            return 5
        elif first_value == 177:
            return 6
        elif first_value == 178:
            return 7
        elif first_value == 179:
            return 8
        elif first_value == 180:
            return 9
    
    def nineteen(first_value):
        if first_value == 181:
            return 0
        elif first_value == 182:
            return 1
        elif first_value == 183:
            return 2
        elif first_value == 184:
            return 3
        elif first_value == 185:
            return 4
        elif first_value == 186:
            return 5
        elif first_value == 187:
            return 6
        elif first_value == 188:
            return 7
        elif first_value == 189:
            return 8
        elif first_value == 190:
            return 9
    
    def twenty(first_value):
        if first_value == 191:
            return 0
        elif first_value == 192:
            return 1
        elif first_value == 193:
            return 2
        elif first_value == 194:
            return 3
        elif first_value == 195:
            return 4
        elif first_value == 196:
            return 5
        elif first_value == 197:
            return 6
        elif first_value == 198:
            return 7
        elif first_value == 199:
            return 8
        elif first_value == 200:
            return 9
        
    def twenty_one(first_value):
        if first_value == 201:
            return 0
        elif first_value == 202:
            return 1
        elif first_value == 203:
            return 2
        elif first_value == 204:
            return 3
        elif first_value == 205:
            return 4
        elif first_value == 206:
            return 5
        elif first_value == 207:
            return 6
        elif first_value == 208:
            return 7
        elif first_value == 209:
            return 8
        elif first_value == 210:
            return 9
        
    def twenty_two(first_value):
        if first_value == 211:
            return 0
        elif first_value == 212:
            return 1
        elif first_value == 213:
            return 2
        elif first_value == 214:
            return 3
        elif first_value == 215:
            return 4
        elif first_value == 216:
            return 5
        elif first_value == 217:
            return 6
        elif first_value == 218:
            return 7
        elif first_value == 219:
            return 8
        elif first_value == 220:
            return 9
        
    def twenty_three(first_value):
        if first_value == 221:
            return 0
        elif first_value == 222:
            return 1
        elif first_value == 223:
            return 2
        elif first_value == 224:
            return 3
        elif first_value == 225:
            return 4
        elif first_value == 226:
            return 5
        elif first_value == 227:
            return 6
        elif first_value == 228:
            return 7
        elif first_value == 229:
            return 8
        elif first_value == 230:
            return 9
    
    def twenty_four(first_value):
        if first_value == 231:
            return 0
        elif first_value == 232:
            return 1
        elif first_value == 233:
            return 2
        elif first_value == 234:
            return 3
        elif first_value == 235:
            return 4
        elif first_value == 236:
            return 5
        elif first_value == 237:
            return 6
        elif first_value == 238:
            return 7
        elif first_value == 239:
            return 8
        elif first_value == 240:
            return 9
    
    def twenty_five(first_value):
        if first_value == 241:
            return 0
        elif first_value == 242:
            return 1
        elif first_value == 243:
            return 2
        elif first_value == 244:
            return 3
        elif first_value == 245:
            return 4
        elif first_value == 246:
            return 5
        elif first_value == 247:
            return 6
        elif first_value == 248:
            return 7
        elif first_value == 249:
            return 8
        elif first_value == 250:
            return 9
    


    def determing_y_coordinates(first_value):
        if first_value >= 1 and first_value <= 10:
            count_y = 0
            return count_y
        
        elif first_value >= 11 and first_value <= 20:
            count_y = 1
            return count_y
        
        elif first_value >= 21 and first_value <= 30:
            count_y = 2
            return count_y
        
        elif first_value >= 31 and first_value <= 40:
            count_y = 3
            return count_y
        
        elif first_value >= 41 and first_value <= 40:
            count_y = 4
            return count_y
        
        elif first_value >= 51 and first_value <= 60:
            count_y = 5
            return count_y
        
        elif first_value >= 61 and first_value <= 70:
            count_y = 6
            return count_y
        
        elif first_value >= 71 and first_value <= 80:
            count_y = 7
            return count_y
        
        elif first_value >= 81 and first_value <= 90:
            count_y = 8
            return count_y
        
        elif first_value >= 91 and first_value <= 100:
            count_y = 9
            return count_y
        
        elif first_value >= 101 and first_value <= 110:
            count_y = 10
            return count_y
        
        elif first_value >= 111 and first_value <= 120:
            count_y = 11
            return count_y
        
        elif first_value >= 121 and first_value <= 130:
            count_y = 12
            return count_y
        
        elif first_value >= 131 and first_value <= 140:
            count_y = 13
            return count_y        
        
        elif first_value >= 141 and first_value <= 150:
            count_y = 14
            return count_y
        
        elif first_value >= 151 and first_value <= 160:
            count_y = 15
            return count_y
        
        elif first_value >= 161 and first_value <= 170:
            count_y = 16
            return count_y
        
        elif first_value >= 171 and first_value <= 180:
            count_y = 17
            return count_y
        
        elif first_value >= 181 and first_value <= 190:
            count_y = 18
            return count_y
        
        elif first_value >= 191 and first_value <= 200:
            count_y = 19
            return count_y
        
        elif first_value >= 201 and first_value <= 210:
            count_y = 20
            return count_y
        
        elif first_value >= 211 and first_value <= 220:
            count_y = 21
            return count_y
        
        elif first_value >= 221 and first_value <= 230:
            count_y = 22
            return count_y
        
        elif first_value >= 231 and first_value <= 240:
            count_y = 23
            return count_y
        
        elif first_value >= 241 and first_value <= 250:
            count_y = 24
            return count_y

        else:
            print(colored("-----------------------------------------------------------------------------------------------\nКритическая ошибка компиляции ассета\n-----------------------------------------------------------------------------------------------" , "red"))