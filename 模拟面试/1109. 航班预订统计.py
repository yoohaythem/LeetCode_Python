class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        start_count = {}
        end_count = {}
        answer = []
        cur = 0
        for booking in bookings:
            start_count[booking[0]] = start_count.get(booking[0],0) + booking[2]
            end_count[booking[1]+1] =  end_count.get(booking[1]+1,0) + booking[2]
        for i in range(1, n+1):
            cur += start_count.get(i,0)
            cur -= end_count.get(i,0)
            answer.append(cur)
        return answer