def sorted_array(a1,a2):
    st=set()
    for i in a1:
        st.add(i)
    for i in a2:
        st.add(i)
    return sorted(st)
a1=[1,3,4,6,3,6]
a2=[2,4,6,7,2,1]
print(sorted_array(a1,a2))