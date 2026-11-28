class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited=[[False]*len(grid[0]) for _ in range(len(grid))]

        island=0

        def dfs(row,col):

            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
                return

            if grid[row][col]=="0" or visited[row][col]:
                return

            visited[row][col]=True

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]=='1' and not visited[row][col]:
                    island+=1

                    dfs(row,col)

        return island


        