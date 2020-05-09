import tweet

def test_results():
    assert tweet.choose_username("realmadrid") == 0
    assert tweet.choose_username2("Cristiano") == 0
    assert tweet.choose_username3("Nationals") == 0


if __name__ == "__main__":
    #test_results()
    # creating thread
    t1 = threading.Thread(target=choose_username, args=(10,))
    t2 = threading.Thread(target=choose_username2, args=(10,))
    t3 = threading.Thread(target=choose_username3, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 2 is completely executed
    t3.join()

