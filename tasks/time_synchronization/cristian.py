from tasks.time_synchronization.clock import Clock

"""
Implement Cristian's algorithm for clock synchronization here.
Use only public interface of the Clock class.
"""
def cristian_time_synchronize(local_clock: Clock, remote_clock: Clock) -> None:
    # TODO: implement me (task 1.1)  
    # Считаем что у нас время монотонное возращается публичным интерйфейсом
    # Пока делал задание 1.2 изучил проект получше, да так и возвращается е мае
    t_0 = local_clock.get_time()
    T = remote_clock.get_time()
    t_1 = local_clock.get_time()
    # (T + (t_1 - t_0)/2) - время какое должно быть, но мы пользуемся offset сооответственно - текущее на процессе
    # RTT = t_1 - t_0 
    local_clock.add_offset((T + (t_1 - t_0)/2) - t_1) 