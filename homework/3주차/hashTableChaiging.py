# HashTable 클래스는 문자열을 key로 입력받는 해쉬 테이블 자료구조를 구현한 것이다. HashTable 클래스는 단순한 해쉬 함수로 인해, 해쉬 충돌이 빈번히 발생한다. 이 단점을 개선하기 위해, Chaining 기법으로 ChainedHashTable을 구현하고자 한다.
# HashTable을 상속하여 해쉬 충돌이 발생해도 정상적으로 동작하는 ChainedHashTable을 완성하시오.

# 간단한 해쉬 테이블 구현
import hashlib
hash_table = [0 for i in range(16)]
chaining_hash_table = [0 for i in range(16)]
# key 얻기


def get_key(data):
    return ord(data[0])


def hash_address(key):
    return key % 16


def store_data(data, value):
    key = get_key(data)
    address = hash_address(key)
    hash_table[address] = value
    return True


def read_data(data):
    key = get_key(data)
    address = hash_address(key)
    if hash_table[address]:
        return hash_table[address]
    else:
        return None


# test
store_data('Dave', '22222222222')
print(hash_table)
print(read_data('Dave'))

# 값이 중복되는 경우
# 1 chaining


def hashlib_get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


def chaining_store_data(data, value):
    key = hashlib_get_key(data)
    address = hash_address(key)
    if chaining_hash_table[address] != 0:
        for item in chaining_hash_table[address]:
            if item[0] == key:
                item[1] = value
                return True
        chaining_hash_table[address].append([key, value])
        return True
    else:
        chaining_hash_table[address] = [[key, value]]
        return True


def chaining_read_data(data):
    key = hashlib_get_key(data)
    address = hash_address(key)
    if chaining_hash_table[address] != 0:
        for item in chaining_hash_table[address]:
            if item[0] == key:
                return item[1]
            else:
                return None
    else:
        return None


chaining_store_data('Dave', '22222222222')
chaining_store_data('DD', '44444444444')
print(chaining_hash_table)
print(chaining_read_data('Dave'))

# 2 linear proving

linear_hash_table = [0 for i in range(16)]


def linear_store_data(data, value):
    key = hashlib_get_key(data)
    address = hash_address(key)
    if linear_hash_table[address] != 0:
        if linear_hash_table[address][0] == key:
            linear_hash_table[address][1] = value
            return True
        else:
            for i in range(address + 1, len(linear_hash_table)):
                if i == 0:
                    linear_hash_table[i] = [key, value]
                    return True
    else:
        linear_hash_table[address] = [key, value]
        return True


def linear_read_data(data):
    key = hashlib_get_key(data)
    address = hash_address(key)
    if linear_hash_table[address] != 0:
        if linear_hash_table[address][0] == key:
            return linear_hash_table[address][1]
        else:
            for index in range(address, len(linear_hash_table)):
                if linear_hash_table[index][0] == key:
                    return linear_hash_table[index][1]
                else:
                    return None
    else:
        return None


print("Linear")
linear_store_data('Dave', '22222222222')
linear_store_data('DD', '44444444444')
print(linear_hash_table)
print(linear_read_data('Dave'))


def hash_func(key):
    return ord(key[0]) % 10


class HashTable:
    def __init__(self):
        self.table = [None]*10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainedHashTable(HashTable):
    pass

# Test code


ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
