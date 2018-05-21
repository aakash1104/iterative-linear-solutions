import random
import sys

def main():

    # Should be exactly 2 arguments
    if (len(sys.argv) != 2):
        print "Usage: gen_matrix.py size of square matrix"
        sys.exit(0)

    file_name = "test_" + sys.argv[1] + ".txt"
    fd = open(file_name, "w")

    for i in range(0, int(sys.argv[1])):
        # Generate a random list of argv[1] numbers
        rand_list = random.sample(range(-5000, 5000), int(sys.argv[1]))

        # Create diagonal dominance by adding other elemens to the diagonal
        for j in range(0, len(rand_list)):
            if (j == i):
                continue
            rand_list[i] += abs(rand_list[j])

        for j in range(0, len(rand_list)):
            if (j == len(rand_list) - 1):
                fd.write("%d" % rand_list[j])
            else:
                fd.write("%d " % rand_list[j])
        fd.write("\n")

    fd.close()

    file_name = "test_vector_" + sys.argv[1] + ".txt"
    fd = open(file_name, "w")
    rand_list = random.sample(range(-5000, 5000), int(sys.argv[1]))

    for j in range(0, len(rand_list)):
        if (j == len(rand_list) - 1):
            fd.write("%d" % rand_list[j])
        else:
            fd.write("%d " % rand_list[j])
    fd.close()
main()
