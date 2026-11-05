-- 코드를 작성해주세요
select i.item_id, item_name
from item_tree t, item_info i
where t.item_id = i.item_id
    and t.parent_item_id is null
order by item_id asc;
