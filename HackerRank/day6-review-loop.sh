# Terminated due to timeout :(

read n

for i in $(seq 1 $n); 
do 
	read -r line;
	for i in $(seq 0 2 ${#line}); 
	do
		c=${line:$i:1}
		printf "$c"
	done

	printf " "
	for i in $(seq 1 2 ${#line}); 
	do
		c=${line:$i:1}
		printf "$c"
	done

	echo
done
