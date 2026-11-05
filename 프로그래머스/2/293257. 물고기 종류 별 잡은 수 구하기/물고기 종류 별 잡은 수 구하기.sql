-- 코드를 작성해주세요
select count(*) as fish_count, n.fish_name
from fish_info i, fish_name_info n
where i.fish_type = n.fish_type
group by i.fish_type
order by fish_count desc;