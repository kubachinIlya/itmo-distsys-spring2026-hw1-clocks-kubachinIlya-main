from typing import Dict

VectorClock = Dict[str, int]

def partial_sort(timestamps: list[VectorClock]) -> list[VectorClock]:
    # TODO: implement me (task 2) 
    def happens_before(vc1: VectorClock, vc2: VectorClock) -> bool:
        """
        Две ноды на вход получаем, их векторные часы и определяем верно ли отношение
        vc1 -> vc2 
        Возвращает true если vc1 -> vc2 
        """  
        # Собираем все уникальные процессы с двух нод, set для словаря - unique список ключей
        # Собираем с обеих нод, потому что не уверены, что они содержат одинаковые процессы
        all_keys = set(vc1) | set(vc2)

        # Для каждого процесса проверяем с помощью генератора условие <=
        # получаем (all) общий результат true or false для проверок по процессам
        le = all(vc1.get(k, 0) <= vc2.get(k, 0) for k in all_keys)

        # аналогично, но условие < и верно хотя бы одно
        lt = any(vc1.get(k, 0) < vc2.get(k, 0) for k in all_keys)

        # le and lt
        # Зачем это нужно: если le = True, но lt = False, то это значит vc1 == vc2 покомпонентно
        # то есть нет отношения vc1 -> vc2
        # le and lt are true - then there is a relation vc1 -> vc2
        return le and lt

    # Элементы которые мы будем просматривать из начального списка
    # делаем именно копию
    remaining = list(timestamps) 
    # результирующий набор векторов result  
    result = []
    # найти минимальный элемент — тот, до которого никто не «произошёл»
    # Для каждой ноды получаем ее индекс и сам вектор
    while remaining:
        for i, vector_value in enumerate(remaining):
            # смотрим есть ли что-то ДО ноды с текущим vector_value , для этого генератор с "remaining" нодами используем ну без текущей выбранной
            if not any(happens_before(other_vector_value, vector_value) for j, other_vector_value in enumerate(remaining) if i != j):
                # если ничего нет, то эту ноду добавляем в результат
                # брейк нужен чтобы с 0 индекса начинать внешний цикл так как элементы сдвинулись (pop)
                result.append(vector_value)
                remaining.pop(i)
                break
        
    return result
 