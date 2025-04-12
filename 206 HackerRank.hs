-- Java code - 31.5%
-- 46 cases passed, others timelimit exceeded
--
-- converted my Java code to Haskell using ChatGPT and got 33.9% 
-- 49 cases passed, others timelimit exceeded


import Data.Char (digitToInt)
import Data.Maybe (listToMaybe)
import System.IO

sqrtFloor :: Integer -> Integer
sqrtFloor x
  | x < 0     = error "Negative argument"
  | x == 0 || x == 1 = x
  | otherwise = newton (x `div` 2 + 1)
  where
    newton y =
      let z = (y + x `div` y) `div` 2
      in if z >= y then adjust y else newton z
    adjust a = if a * a > x then adjust (a - 1) else a

sqrtCeil :: Integer -> Integer
sqrtCeil x = let f = sqrtFloor x in if f * f == x then f else f + 1

fullMatch :: Integer -> String -> Int -> Bool
fullMatch s pat len =
  let sStr = show s
      sPadded = replicate (len - length sStr) '0' ++ sStr
  in length sPadded == len && [ sPadded !! i | i <- [0,2 .. len-1] ] == pat

main :: IO ()
main = do
  contents <- getContents
  let ws = words contents
      n = read (head ws) :: Int
      patList = take n (tail ws)
      patternStr = concat patList
      l = 2 * n - 1
      minSStr = concat [ [c] ++ (if i < n - 1 then "0" else "") | (i, c) <- zip [0..] patternStr ]
      maxSStr = concat [ [c] ++ (if i < n - 1 then "9" else "") | (i, c) <- zip [0..] patternStr ]
      minS = read minSStr :: Integer
      maxS = read maxSStr :: Integer
      lowX = sqrtCeil minS
      highX = sqrtFloor maxS
      d = if n >= 2 then min n 3 else 1
      m = 2 * d - 1
      modInt = 10 ^ m
      modVal = modInt
      validResidues = [ r | r <- [0 .. modInt - 1]
                          , let sq = r * r
                          , all (\j ->
                                   let p   = 2 * (n - 1 - j)
                                       dig = (sq `div` (10 ^ p)) `mod` 10
                                       req = toInteger (digitToInt (patternStr !! j))
                                   in dig == req) [n - d .. n - 1] ]
      candidatesForResidue r =
         let rBI = r
             remVal = lowX `mod` modVal
             firstCandidate = if remVal <= rBI
                                 then lowX - remVal + rBI
                                 else lowX - remVal + modVal + rBI
             gen c | c > highX = [] | otherwise = c : gen (c + modVal)
         in gen firstCandidate
      ans = listToMaybe [ cand
                        | r <- validResidues
                        , cand <- candidatesForResidue r
                        , fullMatch (cand * cand) patternStr l ]
  case ans of
    Just x  -> putStrLn (show x)
    Nothing -> putStrLn "No solution found"
