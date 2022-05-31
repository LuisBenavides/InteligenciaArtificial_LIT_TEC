def main():
    from create_data import main as create_data
    from train import main as train
    from score import main as score
 
    create_data()
    train()
    score()

if __name__ == '__main__':
    main()
