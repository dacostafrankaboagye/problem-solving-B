def arithmetic_arranger(the_list, boolean= False):

    oper = [ "+", "-"]
    v = len(the_list)
    checkerror = 0

    if v > 5:
        print("Error: Too many problems")
    else:
        p = 0
        while v != 0:
            for l in the_list:
                i = l.split(" ")
                for k in i:
                    if not(i[0].isnumeric()) or not(i[2].isnumeric()):
                        print("Error: Numbers must contain only digits.")
                        checkerror +=1
                        break
                    elif i[1] not in oper:
                        print("Error: Operator must be '+' or '-'.")
                        checkerror += 1
                        break
                    elif len(i[0]) > 4 or len(i[2])> 4:
                        print("Numbers cannot be more than four digits.")
                        checkerror += 1
                        break
            v -= 1
            if checkerror > 0:
                break



        if checkerror == 0:

            dash, dashes = "-", []



            position = 0
            # the first row of numbers -- "f_r"
            for w in the_list:
                each_term = the_list[position].split(" ")

                if len(each_term[0]) >= len(each_term[2]):
                    f_r = each_term[0].rjust(len(each_term[0]) + 2)
                    dashes.append(dash * len(f_r))
                    print(f_r, end="\t")
                else:
                    f_r = each_term[0].rjust(len(each_term[2]) + 2)
                    dashes.append(dash * len(f_r))
                    print(f_r, end="\t")

                position += 1
            # the second row of numbers -- "s_r"
            position = 0
            print("\t")
            for w in the_list:
                each_term = the_list[position].split(" ")
                if len(each_term[0]) >= len(each_term[2]):
                    s_r = each_term[2].rjust(len(each_term[0]))
                    print(each_term[1], s_r, end="\t")
                else:
                    s_r = each_term[2].rjust(len(each_term[2]))
                    print(each_term[1], s_r, end="\t")
                position += 1
            # the dashes which is in a list is printed out
            position = 0
            print("\t")
            for w in the_list:
                print(dashes[position], end="\t")
                position += 1


            # the answers or result when a boolean is given
            if boolean == True:
                position = 0
                print("\t")
                for each_item in the_list:
                    each_ = each_item.split(" ")
                    first, last = int(each_[0]), int(each_[2])
                    if each_[1] == "+":
                        print(str(first + last).rjust(len(dashes[position])), end="\t")
                    elif each_[1] == "-":
                        print(str(first - last).rjust(len(dashes[position])), end="\t")
                    position += 1


arithmetic_arranger(["6544 + 783", "7893 - 4", "7 - 80", "89 + 1", "7 + 8789"], True)








