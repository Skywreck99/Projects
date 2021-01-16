(* Assumption: there are no duplicated words *)

type 'a tree = Empty | Cons of 'a tree * 'a * 'a tree

let str_list = ref []

let rec take (num: int) (lst: 'a list) : 'a list =
  match lst with
  | [] -> []
  | x::xs -> if num > 0
             then x::take (num-1) xs
             else []

let rec drop (num: int) (lst: 'a list) : 'a list =
  match lst with
  | [] -> []
  | x::xs -> if num > 0
             then drop (num-1) xs
             else lst

(* Converts a string to a char list *)
let rec explode : string -> char list = function
  | "" -> []
  | s  -> String.get s 0 :: explode (String.sub s 1 ((String.length s) - 1))

(* Converts a char list to a string *)
let rec implode : char list -> string = function
  | [] -> ""
  | c::cs -> String.make 1 c ^ implode cs

(* returns the tree in the given index. The idx must follow the list indexing *)
let rec get_idx (idx: int) (lst: 'a tree list) : 'a tree =
  match lst with
  | [] -> failwith "the list is empty"
  | x::xs -> if idx > 0
             then get_idx (idx-1) xs
             else x

(* Removes the element inside the list *)
let rec remove_elem (elem: char) (lst: char list) : char list =
  match lst with
  | [] -> []
  | x::xs ->
   if x = elem then xs
   else x :: (remove_elem elem xs)

(* Adds the string in the tree *)
let rec add_string_to_tree (str: string) (tree: 'a tree): 'a tree =
  match tree with
  | Empty -> Cons (Empty, str, Empty)
  | Cons (t1, st, t2) -> if str < st
                         then Cons (add_string_to_tree str t1, st, t2)
                         else if str > st
                         then Cons (t1, st, add_string_to_tree str t2)
                         else tree

let read_file (filename:string) : 'a tree =

 (* Gets the word per line in the file and store it in a list and in a tree *)
 let rec read_lines channel sofar =
   try
     let ln = input_line channel
     in match implode (remove_elem '\r' (explode ln)) with
        | ln when ln <> "" -> if String.length ln = 4
                              then str_list := ln::!str_list;
                              if String.length ln = 6
                              then read_lines channel (add_string_to_tree ln sofar)
                              else read_lines channel sofar
        | _ -> read_lines channel sofar
   with
   | End_of_file -> sofar
   | e -> raise e
 in
 try
   let channel = open_in filename
   in read_lines channel Empty
 with
 | e -> raise e


let remove_head (word: char list): char list =
  match word with
  | [] -> []
  | _::xs -> xs

let rec remove_last_elem (word: char list) (accum: char list): char list =
  match word with
  | [] -> accum
  | [y] -> accum
  | x::xs -> remove_last_elem xs (accum @ [x])


(*Assuming w1 has 4 letters and w2 has 6 letters*)
let rec tt_check_words (w1: char list) (w2: char list): bool =
  if w1 = remove_head (remove_last_elem w2 [])
  then true
  else false

let rec assign_words (word: string) (str: string): (string * string) list =
  if String.length str = 6
  then [(word, str)]
  else [(word, (implode (take 6 (explode str))))] @
       assign_words word (implode (drop 6 (explode str)))


let rec string_match (base: 'b)
                     (str: 'a)
                     (func: 'a -> 'a -> 'b -> 'b -> 'b)
                     (tree: 'a tree)
                     : 'b =
   match tree with
   | Empty -> base
   | Cons (t1, st, t2) -> func str st
                          (string_match base str func t1)
                          (string_match base str func t2)



let it_takes_two (filename: string): (string * string) list =
  let rec solve_quiz (lst: string list)
                     (tree: string tree)
                     (accum: (string * string) list)
                     : (string * string) list =

     match lst with
     | [] -> str_list := []; accum
     | four_word::words ->
       let func (str: 'a) (elem: 'a) (t1: string) (t2: string): string =
          if tt_check_words (explode str) (explode elem)
          then t1 ^ elem ^ t2
          else t1 ^ "" ^ t2

       in let word_tt = string_match "" four_word func tree
       in if word_tt <> ""
       then solve_quiz words tree (accum @ assign_words four_word word_tt)
       else solve_quiz words tree accum

   in solve_quiz (List.rev !str_list) (read_file filename) []
