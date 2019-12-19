def bulle_sort
  a = [40,12,23,543,53,2,77,34]
  i =0
  while (i<a.length)
    j=i+1
    while(j<a.length)
      if a[i]>a[j]
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
      end
      j=j+1
    end
    i=i+1
  end 
end
bulle_sort