def minTotalDistance(robot, factory):
    robot.sort()
    factory.sort()

    def distance(x, y):
        return abs(x - y)

    def totalDistance(positions, target):
        total = 0
        for pos in positions:
            total += distance(pos, target)
        return total

    def binarySearch(positions, target):
        left = 0
        right = len(positions) - 1

        while left < right:
            mid = (left + right) // 2
            if positions[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def findClosestFactory(position, factories):
        closest = factories[0][0]
        for factory in factories:
            if distance(position, factory[0]) < distance(position, closest):
                closest = factory[0]
        return closest

    total_distance = 0
    for pos in robot:
        closest_factory = findClosestFactory(pos, factory)
        factory_index = binarySearch(factory, closest_factory)
        total_distance += totalDistance(robot, closest_factory)
        robot = robot[:factory_index] + robot[factory_index + 1:]
        factory[factory_index][1] -= 1
        if factory[factory_index][1] == 0:
            factory = factory[:factory_index] + factory[factory_index + 1:]

    return total_distance
