
# client, date, product, quantity, price
# Jane, 10.11.2018, apple, 1, 4.5



def create_dataset(file):


    try:

        dataset = dict()

        with open(file, 'r') as f:
            file_line = f.readline()

            if not file_line:
                return dataset

            header = file_line.rstrip().split(",")

            file_line = f.readline()
            while file_line:

                [client, date, product, quantity, price] = [element.strip() for element in file_line.rstrip().split(",")]


                if client not in dataset:
                    dataset[client] = dict()

                if date not in dataset[client]:
                    dataset[client][date] = dict()

                dataset[client][date].update({
                                                product: {
                                                            'quantity': quantity,
                                                            'price': price
                                                         }
                                            })



                file_line = f.readline()

        return dataset

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return dict()




# print(create_dataset('../data/orders.csv'))