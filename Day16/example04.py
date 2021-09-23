"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，
不追求最优解，快速找到满意解。
"""
class Thing(object):
    """物品"""
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    # @property是python的一种装饰器，是用来修饰方法的
    # 作用：我们可以使用@property装饰器来创建 只读属性
    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight

def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')

if __name__ == '__main__':
    main()
