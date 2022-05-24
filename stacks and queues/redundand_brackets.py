def redundant(exp):
    st = []
    flag = True
    for char in exp:
        
        if char == ")":
            top = st[-1]
            st.pop()
            flag = True
          
            while(top!= '('):
                if (top == '+' or top == '-' or top == '*' or top == '/'):
                    flag = False
                
                top = st[-1]
                st.pop()
                
            if(flag == True):
                return True
        else:
            st.append(char)
    return False            
            
                  
if __name__ == '__main__':
    Str = "((a+b))"
    print(redundant(Str))
 
    Str = "(a+(b)/c)"
    print(redundant(Str))
 
    Str = "(a+b*(c-d))"
    print(redundant(Str))
            
            
            
        