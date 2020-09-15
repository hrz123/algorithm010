# mysql.py


# 除了update语句外，select语句如果加锁，也是当前读
# 一个是获取读锁
# select k from t where id=1 lock in share mode;
# 一个是获取写锁
# select k from t where id=1 for update;

def main():
    pass


if __name__ == '__main__':
    main()
